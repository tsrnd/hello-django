CREATE TABLE IF NOT EXISTS tbl_snipplet (
    id SERIAL PRIMARY KEY,
    title character varying(100),
    code text,
    linenos boolean DEFAULT false,
    language character varying(100),
    style character varying(100)
);