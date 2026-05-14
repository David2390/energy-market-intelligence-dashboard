import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection
user = "postgres"
password = "YourPassword"
host = "localhost"
port = "5432"
database = "oil_market"

# Create engine
engine = create_engine(
    f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
)

# Commodity tickers
tickers = {
    "WTI_Crude": "CL=F",
    "Brent_Crude": "BZ=F",
    "Gasoline": "RB=F",
    "Heating_Oil": "HO=F",
    "Natural_Gas": "NG=F"
}

all_data = []

# Download data
for name, ticker in tickers.items():

    print(f"Downloading {name}...")

    df = yf.download(
        ticker,
        period="5y",
        interval="1d"
    )

    # Reset index
    df.reset_index(inplace=True)

    # Flatten MultiIndex columns
    df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]

    # Add commodity name
    df["Commodity"] = name

    all_data.append(df)

# Combine all dataframes
final_df = pd.concat(all_data, ignore_index=True)

# Load into PostgreSQL
final_df.to_sql(
    "commodity_prices",
    con=engine,
    if_exists="replace",
    index=False
)

print("\nData loaded into PostgreSQL successfully!")
print(final_df.head())