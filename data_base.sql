create database medical_warehouse;

create table medical_product(
	id serial primary key,
	name varchar(50),
	count int,
	price float,
	time varchar(50)
);

create table costumer(
	id serial primary key,
	first_name varchar(50),
	second_name varchar(50),
	product_name varchar(50),
	product_count int,
	product_price float,
	product_time varchar(50)
);


drop table costumer;

INSERT INTO costumer (first_name, second_name, product_name, product_count, product_price, product_time) VALUES ('Sam', 'Watsob', 'Paracetamol', 1, (SELECT price FROM medical_product AS m join costumer AS c ON m.name = c.product_name WHERE m.name = c.product_name), '2024-02-24 12:20:40');
select * from costumer;

select * from medical_product;

INSERT INTO medical_product (name, count, price, time) VALUES ('Paracetamol', 5, 5.5, '2024-02-24 12:20:40');
