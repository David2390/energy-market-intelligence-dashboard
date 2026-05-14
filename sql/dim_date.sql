CREATE TABLE IF NOT EXISTS public.dim_date
(
    date_id integer NOT NULL DEFAULT nextval('dim_date_date_id_seq'::regclass),
    full_date date,
    year integer,
    month integer,
    day integer,
    weekday character varying(20) COLLATE pg_catalog."default",
    CONSTRAINT dim_date_pkey PRIMARY KEY (date_id),
    CONSTRAINT dim_date_full_date_key UNIQUE (full_date)
)

TABLESPACE pg_default;

ALTER TABLE public.dim_date
    OWNER to postgres;
