-- Table Definition ----------------------------------------------

CREATE TABLE IF NOT EXISTS tbl_snipplet (
    id SERIAL PRIMARY KEY,
    title character varying(100),
    code text,
    linenos boolean DEFAULT false,
    language character varying(100),
    style character varying(100)
);

-- Table POST for join data.
CREATE TABLE IF NOT EXISTS tbl_post (
    id SERIAL PRIMARY KEY,
    title character varying(200) NOT NULL,
    content text,
    snipid integer NOT NULL REFERENCES tbl_snipplet(id)
);