CREATE TABLE IF NOT EXISTS public.commodity_news
(
    news_id integer NOT NULL DEFAULT nextval('commodity_news_news_id_seq'::regclass),
    commodity_name character varying(50) COLLATE pg_catalog."default",
    news_date timestamp without time zone,
    headline text COLLATE pg_catalog."default",
    source text COLLATE pg_catalog."default",
    url text COLLATE pg_catalog."default",
    search_query text COLLATE pg_catalog."default",
    loaded_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT commodity_news_pkey PRIMARY KEY (news_id),
    CONSTRAINT uq_commodity_news_commodity_url UNIQUE (commodity_name, url)
)

TABLESPACE pg_default;

ALTER TABLE public.commodity_news
    OWNER to postgres;
