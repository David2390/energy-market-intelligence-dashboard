CREATE TABLE IF NOT EXISTS public.commodity_correlation
(
    commodity_1 text COLLATE pg_catalog."default",
    commodity_2 text COLLATE pg_catalog."default",
    correlation double precision
)

TABLESPACE pg_default;

ALTER TABLE public.commodity_correlation
    OWNER to postgres;
