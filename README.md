# Energy Market Intelligence Dashboard

Enterprise-style Energy Market Intelligence Dashboard built with Python, PostgreSQL, Machine Learning, and Power BI. The platform combines automated ETL pipelines, financial time-series analysis, forecasting models, and executive reporting capabilities into a unified analytics solution.

---

# Project Overview

This project was developed to provide centralized monitoring and analysis of key energy commodities including:

- WTI Crude
- Brent Crude
- Gasoline
- Heating Oil
- Natural Gas

The dashboard enables users to monitor:

- Historical price trends
- Commodity correlations
- Market volatility
- Price spreads
- Trading volume
- Machine learning forecasts
- Dynamic market insights
- Automated commodity news

The solution simulates a real-world enterprise analytics platform with automated data refresh pipelines and executive reporting modules.

---

# Technology Stack

| Layer | Technology |
|---|---|
| Programming Language | Python |
| Database | PostgreSQL |
| Visualization | Power BI |
| Data Processing | Pandas |
| Machine Learning | Scikit-learn |
| Data Source | Yahoo Finance API |
| ORM / DB Connection | SQLAlchemy |
| Forecasting Model | Random Forest Regressor |

---

# Dashboard Modules

## 1. Executive Overview
High-level executive KPI monitoring including:

- Latest commodity prices
- Daily percentage changes
- Moving averages
- Volatility indicators
- Executive summary visuals

---

## 2. Daily Price Trends
Historical market analysis including:

- OHLC analysis
- Trading volume
- Moving averages (7D / 30D / 90D)
- Commodity-specific filtering
- Dynamic market news integration

---

## 3. Commodity Comparison & Correlation Analysis
Cross-commodity analysis including:

- Correlation heatmaps
- Indexed commodity performance
- Brent-WTI spread analysis
- Relative market behavior

---

## 4. Volatility Analysis
Market instability analysis including:

- Rolling 30-day volatility
- Daily price range analysis
- Volatility ranking by commodity
- Largest price swing detection
- Dynamic executive insights

---

## 5. Forecasting
Machine learning forecasting module including:

- 30-day WTI crude oil forecast
- Historical vs forecast visualization
- Actual vs predicted validation
- Forecast confidence range
- MAE validation metrics
- Automated forecast narrative generation

---

## 6. Version & Technical Documentation
Internal platform governance page including:

- Release history
- Technical architecture
- Core modules
- Forecast methodology
- Planned future improvements

---

# Technical Architecture

```text
Yahoo Finance API
        ↓
Python ETL Pipelines
        ↓
PostgreSQL Database
        ↓
Power BI Semantic Model
        ↓
Executive Dashboard
```

---

# Forecasting Methodology

## Model
Random Forest Regressor

## Features Used
- Historical close prices
- Lagged price features
- Moving averages
- Rolling volatility
- Daily returns
- Price range indicators

## Validation Metric
- Mean Absolute Error (MAE): 2.05

## Forecast Horizon
- 30 Days

---

# Automated ETL Pipeline

The project includes automated Python ETL processes for:

- Daily commodity price extraction
- Data transformation
- PostgreSQL loading
- News ingestion
- Forecast generation
- Correlation analysis updates

---

# Screenshots

## Executive Overview
![Executive Overview](images/executive_overview.png)

## Daily Price Trends
![Daily Price Trends](images/daily_price_trends.png)

## Commodity Comparison
![Commodity Comparison](images/commodity_comparison.png)

## Volatility Analysis
![Volatility Analysis](images/volatility_analysis.png)

## Forecasting
![Forecasting](images/forecasting.png)

## Version & Technical Notes
![Version Page](images/version_page.png)

---

# Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/energy-market-intelligence-dashboard.git
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure PostgreSQL Connection

Update your database credentials inside the ETL scripts:

```python
DATABASE_URL = "postgresql+psycopg2://postgres:YOUR_PASSWORD@localhost:5432/oil_market"
```

---

# Future Enhancements

Planned improvements include:

- Real-time market streaming
- LSTM forecasting models
- Prophet forecasting
- Macroeconomic indicator integration
- Airline fuel hedging simulations
- OPEC event tracking
- News sentiment analysis
- Cloud-hosted deployment pipelines

---

# Disclaimer

This project was developed for analytical, educational, and portfolio demonstration purposes. Forecasting results are based on historical market behavior and should not be interpreted as financial advice.

---

# Developed By

## David Méndez
Data Analytics & Market Intelligence Portfolio Project
