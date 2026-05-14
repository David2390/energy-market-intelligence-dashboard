-- View: public.vw_commodity_news

-- DROP VIEW public.vw_commodity_news;

CREATE OR REPLACE VIEW public.vw_commodity_news AS
 SELECT dc.commodity_id,
    cn.news_id,
    cn.commodity_name,
    cn.news_date,
    cn.headline,
    cn.source,
    cn.url,
    cn.search_query,
    cn.loaded_at
   FROM commodity_news cn
     JOIN dim_commodity dc ON cn.commodity_name::text =
        CASE
            WHEN dc.commodity_name::text = 'Heating_Oil'::text THEN 'Heating Oil'::character varying
            WHEN dc.commodity_name::text = 'Brent_Crude'::text THEN 'Brent Crude'::character varying
            WHEN dc.commodity_name::text = 'WTI_Crude'::text THEN 'WTI Crude'::character varying
            WHEN dc.commodity_name::text = 'Natural_Gas'::text THEN 'Natural Gas'::character varying
            ELSE dc.commodity_name
        END::text;

ALTER TABLE public.vw_commodity_news
    OWNER TO postgres;
