import pandas as pd
from sqlalchemy import create_engine
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

# PostgreSQL connection
DATABASE_URL = "postgresql+psycopg2://postgres:YourPassword!@localhost:5432/oil_market"

engine = create_engine(DATABASE_URL)

# Load feature dataset
query = """
SELECT *
FROM vw_wti_features
ORDER BY full_date
"""

df = pd.read_sql(query, engine)

# Convert date column
df["full_date"] = pd.to_datetime(df["full_date"])

# Remove nulls from rolling/lag features
df = df.dropna().copy()

# Define features
features = [
    "lag_1",
    "ma_7",
    "ma_30",
    "volatility_30d"
]

# Train model using all historical data
X = df[features]
y = df["close_price"]

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X, y)

# Forecast settings
future_days = 30

# Copy historical data for recursive forecasting
forecast_df = df[["full_date", "close_price"]].copy()

future_predictions = []
future_dates = []

last_date = forecast_df["full_date"].max()

# Recursive forecasting loop
for i in range(future_days):

    next_date = last_date + pd.Timedelta(days=1)

    lag_1 = forecast_df["close_price"].iloc[-1]
    ma_7 = forecast_df["close_price"].tail(7).mean()
    ma_30 = forecast_df["close_price"].tail(30).mean()
    volatility_30d = forecast_df["close_price"].tail(30).std()

    next_features = pd.DataFrame({
        "lag_1": [lag_1],
        "ma_7": [ma_7],
        "ma_30": [ma_30],
        "volatility_30d": [volatility_30d]
    })

    next_prediction = model.predict(next_features)[0]

    future_predictions.append(next_prediction)
    future_dates.append(next_date)

    new_row = pd.DataFrame({
        "full_date": [next_date],
        "close_price": [next_prediction]
    })

    forecast_df = pd.concat(
        [forecast_df, new_row],
        ignore_index=True
    )

    last_date = next_date

# Create forecast dataframe
future_forecast = pd.DataFrame({
    "Date": future_dates,
    "Forecast_Price": future_predictions
})

print(future_forecast)

# Plot historical + forecast
# plt.figure(figsize=(16, 8))

# plt.plot(
#     df["full_date"],
#     df["close_price"],
#     label="Historical"
# )

# plt.plot(
#     future_forecast["Date"],
#     future_forecast["Forecast_Price"],
#     label="30-Day Forecast"
# )

# plt.title("WTI Crude Oil 30-Day Future Forecast")
# plt.xlabel("Date")
# plt.ylabel("WTI Price")

# plt.xticks(rotation=45)

# plt.legend()
# plt.tight_layout()
# plt.show()

# Filter historical data to show only 2026
plot_start_date = "2026-01-01"

historical_plot_df = df[df["full_date"] >= plot_start_date]

# Plot historical 2026 + forecast
plt.figure(figsize=(16, 8))

plt.plot(
    historical_plot_df["full_date"],
    historical_plot_df["close_price"],
    label="Historical 2026"
)

plt.plot(
    future_forecast["Date"],
    future_forecast["Forecast_Price"],
    label="30-Day Forecast"
)

plt.title("WTI Crude Oil 30-Day Future Forecast - 2026 View")
plt.xlabel("Date")
plt.ylabel("WTI Price")

plt.xticks(rotation=45)

plt.legend()
plt.tight_layout()
plt.show()

future_forecast.to_sql(
    "forecast_wti_30_days",
    con=engine,
    if_exists="replace",
    index=False
)

# Save forecast into PostgreSQL
future_forecast.to_sql(
    "forecast_wti_30_days",
    con=engine,
    if_exists="replace",
    index=False
)

print("Forecast table loaded into PostgreSQL successfully.")

# Rename columns for PostgreSQL / Power BI
future_forecast = future_forecast.rename(columns={
    "Date": "forecast_date",
    "Forecast_Price": "predicted_price"
})

# Add model metadata
future_forecast["commodity_name"] = "WTI Crude"
future_forecast["model_name"] = "Random Forest"
future_forecast["forecast_horizon_days"] = 30
future_forecast["mae"] = 2.05
future_forecast["loaded_at"] = pd.Timestamp.now()

# Save forecast into PostgreSQL
future_forecast.to_sql(
    "fct_wti_forecast",
    con=engine,
    if_exists="replace",
    index=False
)

print("Forecast table loaded into PostgreSQL successfully.")
print(future_forecast)