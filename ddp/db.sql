create table tbl_topics(
    id serial PRIMARY KEY,
    text VARCHAR (50) UNIQUE NOT NULL)

DROP TABLE  IF EXISTS tbl_posts

create table tbl_posts(
    id serial PRIMARY KEY,
    text VARCHAR (50) UNIQUE NOT NULL,
    topic_id INTEGER REFERENCES tbl_topics(id))

insert into tbl_topics(text) values('The thirth topic')
insert into tbl_posts(text, topic_id) values ('Next post', 2)