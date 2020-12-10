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