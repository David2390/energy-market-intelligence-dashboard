-- Table: public.dim_commodity

-- DROP TABLE IF EXISTS public.dim_commodity;

CREATE TABLE IF NOT EXISTS public.dim_commodity
(
    commodity_id integer NOT NULL DEFAULT nextval('dim_commodity_commodity_id_seq'::regclass),
    commodity_name character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT dim_commodity_pkey PRIMARY KEY (commodity_id),
    CONSTRAINT dim_commodity_commodity_name_key UNIQUE (commodity_name)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.dim_commodity
    OWNER to postgres;