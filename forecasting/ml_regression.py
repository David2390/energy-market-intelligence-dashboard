import pandas as pd
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

# PostgreSQL connection
DATABASE_URL = "postgresql+psycopg2://postgres:YourPassword!@localhost:5432/oil_market"

engine = create_engine(DATABASE_URL)

# Load features from SQL view
query = """
SELECT *
FROM vw_wti_features
ORDER BY full_date
"""

df = pd.read_sql(query, engine)

# Convert date column to datetime
df['full_date'] = pd.to_datetime(df['full_date'])

# Remove nulls created by rolling calculations
df = df.dropna()

# Features for machine learning
X = df[
    [
        'lag_1',
        'ma_7',
        'ma_30',
        'volatility_30d'
    ]
]

# Target variable
y = df['close_price']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    shuffle=False
)

# Random Forest model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Generate predictions
predictions = model.predict(X_test)

# Accuracy metric
mae = mean_absolute_error(y_test, predictions)

# Create validation table for Power BI
validation_df = pd.DataFrame({
    "validation_date": df.loc[X_test.index, "full_date"].values,
    "actual_price": y_test.values,
    "predicted_price": predictions,
    "model_name": "Random Forest"
})

validation_df["error"] = validation_df["actual_price"] - validation_df["predicted_price"]
validation_df["absolute_error"] = validation_df["error"].abs()
validation_df["mae"] = mae
validation_df["loaded_at"] = pd.Timestamp.now()

# Save validation results into PostgreSQL
validation_df.to_sql(
    "fct_wti_model_validation",
    con=engine,
    if_exists="replace",
    index=False
)

print("Model validation table loaded into PostgreSQL successfully.")

print(f"Random Forest MAE: {mae:.2f}")

# Retrieve dates corresponding to test set
# test_dates = df.iloc[X_test.index]['full_date']
test_dates = df.loc[X_test.index, 'full_date']

# Plot results
plt.figure(figsize=(16,8))

# Actual prices
plt.plot(
    test_dates,
    y_test,
    label='Actual'
)

# Predicted prices
plt.plot(
    test_dates,
    predictions,
    label='Predicted'
)

# Titles and labels
plt.title('Random Forest WTI Prediction')

plt.xlabel('Date')
plt.ylabel('WTI Price')

# Rotate dates for readability
plt.xticks(rotation=45)

# Legend
plt.legend()

# Improve spacing
plt.tight_layout()

# Show chart
plt.show()