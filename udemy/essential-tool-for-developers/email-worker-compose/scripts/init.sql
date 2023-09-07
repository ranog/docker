create database email_sender;

\c email_sender;

create table emails (
    id serial not null primary key,
    date timestamp not null default now(),
    email varchar(255) not null,
    subject varchar(255) not null,
    message varchar(255) not null
);
