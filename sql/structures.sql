drop database if exists nyctaxi;
create database nyctaxi;
use nyctaxi;

create table nyctaxi.trips (
    vendor_id varchar(255),
    pickup_datetime varchar(255),
    dropoff_datetime varchar(255),
    passenger_count varchar(255),
    trip_distance varchar(255),
    pickup_longitude varchar(255),
    pickup_latitude varchar(255),
    rate_code varchar(255),
    store_and_fwd_flag varchar(255),
    dropoff_longitude varchar(255),
    dropoff_latitude varchar(255),
    payment_type varchar(255),
    fare_amount varchar(255),
    surcharge varchar(255),
    tip_amount varchar(255),
    tolls_amount varchar(255),
    total_amount varchar(255)
);

create table nyctaxi.payment_lookup (
    payment_type varchar(255),
    payment_lookup varchar(255)
);

create table nyctaxi.vendor_lookup (
    vendor_id varchar(255),
    name varchar(255),
    address varchar(255),
    city varchar(255),
    state varchar(255),
    zip varchar(255),
    country varchar(255),
    contact varchar(255),
    current varchar(255)
);