CREATE TABLE IF NOT EXISTS public.fct_wti_model_validation
(
    validation_date timestamp without time zone,
    actual_price double precision,
    predicted_price double precision,
    model_name text COLLATE pg_catalog."default",
    error double precision,
    absolute_error double precision,
    mae double precision,
    loaded_at timestamp without time zone
)

TABLESPACE pg_default;

ALTER TABLE public.fct_wti_model_validation
    OWNER to postgres;
