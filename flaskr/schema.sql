-- This file should run once to create the tables and fill data.

-- SQL statements for creating the tables.

CREATE TABLE car(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    model CHAR(20),
    year INTEGER(4),
    FOREIGN KEY (company_id) references company(id)
);

CREATE TABLE company(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    logo_url TEXT,
    name CHAR(20)
);

CREATE TABLE option (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    display TEXT
);

CREATE TABLE vote(
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     option_id INTEGER,
     car_id INTEGER,
     value TEXT,
     FOREIGN KEY (option_id) references option(id),
     FOREIGN KEY (car_id) references car(id)
 );

INSERT INTO company(logo_url, name) VALUES ('https://logos-download.com/wp-content/uploads/2016/03/Hyundai_Motor_Company_logo.png', 'Hyndai');
INSERT INTO company(logo_url, name) VALUES ('https://logodownload.org/wp-content/uploads/2014/02/ford-logo-1-1.png', 'Ford');
INSERT INTO company(logo_url, name) VALUES ('https://logos-world.net/wp-content/uploads/2020/04/Toyota-Logo.png', 'Toyota');


INSERT INTO car(company_id, model, year) VALUES (1,'Sonata', 2020), (1, 'Avante', 2020), (2, 'Fusion', 2020), (3, 'Camry', 2020), (3,'Prius', 2020);

INSERT INTO option(name) VALUES ('leather'), ('color'), ('is_popular');