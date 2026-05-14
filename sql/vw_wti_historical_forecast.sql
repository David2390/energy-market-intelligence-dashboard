-- View: public.vw_wti_historical_forecast

-- DROP VIEW public.vw_wti_historical_forecast;

CREATE OR REPLACE VIEW public.vw_wti_historical_forecast AS
 SELECT d.full_date AS price_date,
    'Historical WTI'::text AS series,
    f.close_price AS price
   FROM fact_commodity_prices f
     JOIN dim_date d ON f.date_id = d.date_id
     JOIN dim_commodity c ON f.commodity_id = c.commodity_id
  WHERE c.commodity_name::text = 'WTI_Crude'::text
UNION ALL
 SELECT fct_wti_forecast.forecast_date::date AS price_date,
    'Forecasted WTI'::text AS series,
    fct_wti_forecast.predicted_price AS price
   FROM fct_wti_forecast;

ALTER TABLE public.vw_wti_historical_forecast
    OWNER TO postgres;
