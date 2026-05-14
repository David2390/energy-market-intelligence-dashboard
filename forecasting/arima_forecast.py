import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error

# PostgreSQL connection
DATABASE_URL = "postgresql+psycopg2://postgres:YourPassword!@localhost:5432/oil_market"

engine = create_engine(DATABASE_URL)

# Load data
query = """
SELECT
    full_date,
    wti_crude
FROM vw_commodity_price_comparison
ORDER BY full_date
"""

df = pd.read_sql(query, engine)

# Prepare data
df['full_date'] = pd.to_datetime(df['full_date'])

df.set_index('full_date', inplace=True)

df = df.asfreq('D')

df['wti_crude'] = df['wti_crude'].interpolate()

# Train/test split
train_size = int(len(df) * 0.8)

train = df.iloc[:train_size]
test = df.iloc[train_size:]

# ARIMA model
model = ARIMA(
    train['wti_crude'],
    order=(5,1,2)
)

fit_model = model.fit()

# Forecast
forecast = fit_model.forecast(steps=len(test))

forecast.index = test.index

# Accuracy
mae = mean_absolute_error(
    test['wti_crude'],
    forecast
)

print(f"ARIMA MAE: {mae:.2f}")

# Plot
plt.figure(figsize=(14,7))

plt.plot(train.index, train['wti_crude'], label='Train')

plt.plot(test.index, test['wti_crude'], label='Actual')

plt.plot(forecast.index, forecast, label='ARIMA Forecast')

plt.title("ARIMA Forecast Validation")

plt.legend()

plt.tight_layout()

plt.show()