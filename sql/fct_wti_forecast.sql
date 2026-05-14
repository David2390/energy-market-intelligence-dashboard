CREATE TABLE IF NOT EXISTS public.fct_wti_forecast
(
    forecast_date timestamp without time zone,
    predicted_price double precision,
    commodity_name text COLLATE pg_catalog."default",
    model_name text COLLATE pg_catalog."default",
    forecast_horizon_days bigint,
    mae double precision,
    loaded_at timestamp without time zone
)

TABLESPACE pg_default;

ALTER TABLE public.fct_wti_forecast
    OWNER to postgres;
