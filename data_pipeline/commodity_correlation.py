import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg2://postgres:YourPassword@localhost:5432/oil_market"

engine = create_engine(DATABASE_URL)

query = """
SELECT *
FROM vw_commodity_price_comparison
ORDER BY full_date
"""

df = pd.read_sql(query, engine)

price_cols = [
    "wti_crude",
    "brent_crude",
    "gasoline",
    "heating_oil",
    "natural_gas"
]

corr = df[price_cols].corr()

corr_long = corr.reset_index().melt(
    id_vars="index",
    var_name="commodity_2",
    value_name="correlation"
)

corr_long = corr_long.rename(
    columns={"index": "commodity_1"}
)

corr_long.to_sql(
    "commodity_correlation",
    con=engine,
    if_exists="replace",
    index=False
)

print("Correlation table loaded successfully.")
print(corr_long)