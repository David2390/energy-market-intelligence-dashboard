\# Architecture Notes



\## Project Architecture



The Energy Market Intelligence Dashboard is designed as an end-to-end analytics solution that combines data extraction, database modeling, machine learning forecasting, and executive reporting.



The solution follows this architecture:



```text

Yahoo Finance API

&#x20;       ↓

Python ETL Pipelines

&#x20;       ↓

PostgreSQL Data Warehouse

&#x20;       ↓

Power BI Semantic Model

&#x20;       ↓

Executive Analytics Dashboard

```



\## Data Pipeline Layer



Python scripts are used to extract, transform, and load commodity market data into PostgreSQL.



Main responsibilities:



\- Extract historical commodity prices

\- Retrieve daily market updates

\- Load clean data into PostgreSQL

\- Generate forecast outputs

\- Load model validation results

\- Retrieve commodity-related news

\- Generate commodity correlation tables



Key scripts:

| Script                     | Purpose                                                    |

| -------------------------- | ---------------------------------------------------------- |

| `crude\_oil\_prices.py`      | Extracts commodity price data and loads it into PostgreSQL |

| `commodity\_news\_etl.py`    | Retrieves latest commodity-related news headlines          |

| `commodity\_correlation.py` | Generates commodity correlation table                      |

| `ml\_regression.py`         | Trains Random Forest model and stores validation results   |

| `future\_forecast.py`       | Generates 30-day WTI forecast                              |





\## Database Layer

PostgreSQL is used as the analytical storage layer.



The database includes:



\- Raw ingestion tables

\- Dimension tables

\- Fact tables

\- Analytical views

\- Forecast tables

\- Model validation tables

\- News tables



Main modeling approach:



\- dim\_date

\- dim\_commodity

\- fact\_commodity\_prices



This structure supports a star-schema style model suitable for Power BI reporting.



\## Power BI Semantic Model

Power BI connects to PostgreSQL and uses the prepared tables and views to build analytical pages.



Main report pages:

| Page                 | Purpose                                                        |

| -------------------- | -------------------------------------------------------------- |

| Executive Overview   | High-level KPI monitoring                                      |

| Daily Price Trends   | Price movements, moving averages, OHLC trends, and volume      |

| Commodity Comparison | Correlation analysis, Brent-WTI spread, indexed performance    |

| Volatility Analysis  | Rolling volatility, price swings, and risk monitoring          |

| Forecasting          | 30-day WTI forecast, validation, and forecast confidence range |

| Version              | Documentation, version history, and technical architecture     |



\## Forecasting Architecture

The forecasting module uses a Random Forest Regressor trained on engineered time-series features.



Features include:



\- Lagged close prices

\- Moving averages

\- Rolling volatility

\- Daily price changes

\- Price range indicators



The model generates:



\- 30-day WTI forecast

\- Actual vs predicted validation table

\- Mean Absolute Error (MAE)

\- Forecast upper and lower ranges based on MAE



The forecast is not financial advice and is intended for analytical demonstration.



\## News Integration

Commodity-related headlines are retrieved using a Python ETL script and stored in PostgreSQL.



Power BI uses this table to display dynamic news based on the selected commodity.



This adds external market context to the dashboard and supports executive interpretation.



\## Automation Strategy

The intended refresh process is:



Scheduled Python ETL

&#x20;       ↓

PostgreSQL table refresh

&#x20;       ↓

Power BI dataset refresh

&#x20;       ↓

Updated dashboard visuals



In a production environment, this could be automated using:



\- Windows Task Scheduler

\- Apache Airflow

\- GitHub Actions

\- Cloud-hosted database

\- Power BI Service scheduled refresh

\- On-premises data gateway



\## Design Principles

This project was designed around the following principles:



\- Clear executive storytelling

\- Separation between raw data and analytical models

\- Reusable SQL views

\- Dynamic DAX insights

\- Explainable forecasting

\- Portfolio-quality documentation

\- Enterprise-style dashboard structure



\## Limitations

Current limitations include:



\- Forecasts are based only on historical price behavior

\- The model does not account for geopolitical events

\- Macroeconomic indicators are not yet included

\- News sentiment is not yet analyzed

\- Forecast confidence range is approximated using MAE

\- Local PostgreSQL setup requires local refresh configuration



\## Future Improvements

Planned improvements include:



\- Prophet forecasting model

\- LSTM neural network forecasting

\- News sentiment analysis

\- OPEC event tracking

\- Macroeconomic indicators

\- Airline fuel hedging simulations

\- Cloud deployment

\- Automated CI/CD refresh workflow

