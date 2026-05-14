import feedparser
import psycopg2
from datetime import datetime
from urllib.parse import quote_plus

# PostgreSQL connection
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "oil_market",
    "user": "postgres",
    "password": "YourPassword"
}

# Commodity search terms
commodities = {
    "WTI Crude": "WTI crude oil price news",
    "Brent Crude": "Brent crude oil price news",
    "Gasoline": "gasoline futures price news",
    "Heating Oil": "heating oil futures price news",
    "Natural Gas": "natural gas price news"
}


def create_table():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS commodity_news (
            news_id SERIAL PRIMARY KEY,
            commodity_name VARCHAR(50),
            news_date TIMESTAMP,
            headline TEXT,
            source TEXT,
            url TEXT,
            search_query TEXT,
            loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE (commodity_name, url)
        );
    """)

    conn.commit()
    cur.close()
    conn.close()


def fetch_google_news(commodity_name, search_query):
    encoded_query = quote_plus(search_query)

    rss_url = (
        f"https://news.google.com/rss/search?"
        f"q={encoded_query}&hl=en-US&gl=US&ceid=US:en"
    )

    feed = feedparser.parse(rss_url)

    news_records = []

    for entry in feed.entries[:10]:
        headline = entry.get("title", "")
        url = entry.get("link", "")
        source = entry.get("source", {}).get("title", "Unknown")

        published = entry.get("published_parsed")

        if published:
            news_date = datetime(*published[:6])
        else:
            news_date = datetime.now()

        news_records.append({
            "commodity_name": commodity_name,
            "news_date": news_date,
            "headline": headline,
            "source": source,
            "url": url,
            "search_query": search_query
        })

    return news_records


def insert_news(records):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    insert_query = """
        INSERT INTO commodity_news (
            commodity_name,
            news_date,
            headline,
            source,
            url,
            search_query
        )
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (commodity_name, url) DO NOTHING;
    """

    for record in records:
        cur.execute(
            insert_query,
            (
                record["commodity_name"],
                record["news_date"],
                record["headline"],
                record["source"],
                record["url"],
                record["search_query"]
            )
        )

    conn.commit()
    cur.close()
    conn.close()


def main():
    create_table()

    all_records = []

    for commodity_name, search_query in commodities.items():
        print(f"Fetching news for {commodity_name}...")

        records = fetch_google_news(
            commodity_name,
            search_query
        )

        all_records.extend(records)

    insert_news(all_records)

    print(f"News ETL completed. {len(all_records)} records processed.")


if __name__ == "__main__":
    main()