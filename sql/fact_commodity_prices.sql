CREATE TABLE IF NOT EXISTS public.fact_commodity_prices
(
    fact_id integer NOT NULL DEFAULT nextval('fact_commodity_prices_fact_id_seq'::regclass),
    date_id integer,
    commodity_id integer,
    open_price double precision,
    high_price double precision,
    low_price double precision,
    close_price double precision,
    volume bigint,
    CONSTRAINT fact_commodity_prices_pkey PRIMARY KEY (fact_id),
    CONSTRAINT fk_commodity FOREIGN KEY (commodity_id)
        REFERENCES public.dim_commodity (commodity_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_date FOREIGN KEY (date_id)
        REFERENCES public.dim_date (date_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE public.fact_commodity_prices
    OWNER to postgres;
