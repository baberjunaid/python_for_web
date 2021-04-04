create database python_for_web;
use python_for_web;
CREATE TABLE students (
    id int NOT NULL AUTO_INCREMENT,
    full_name VARCHAR(100),
    email VARCHAR(100),
    batch_title varchar(100),
    date_created  DATETIME DEFAULT   CURRENT_TIMESTAMP,
PRIMARY KEY (id)
);

insert into students(full_name, email, batch_title) values ('M Raza Khan', 'raza@gmail.com', 'BSCS');
insert into students(full_name, email, batch_title) values ('Azhar Khan', 'azhar@gmail.com', 'BSIT');
insert into students(full_name, email, batch_title) values ('Wateen Khan', 'wateen@gmail.com', 'BSCS');
insert into students(full_name, email, batch_title) values ('Zaheer Khan', 'zaheer@gmail.com', 'BSCS');

