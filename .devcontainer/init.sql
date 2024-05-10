\c postgres
create schema pytb;

create table pytb.user_transactions (
    user_id int,
    amount int,
    created_at timestamp without time zone not null default (current_timestamp at time zone 'utc')

);