-- SCHEMA: store_db

CREATE SCHEMA IF NOT EXISTS store_db
    AUTHORIZATION alejandrosolanovega;

-- Indicamos que todo lo siguiente se cree dentro de store_db
SET search_path TO store_db;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    code VARCHAR(50) NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    stock INTEGER NOT NULL DEFAULT 0,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE bills (
    id SERIAL PRIMARY KEY,
    date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    user_id INTEGER NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE product_bill (
    id SERIAL PRIMARY KEY,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    bill_id INTEGER NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (bill_id) REFERENCES bills(id)
);

ALTER TABLE bills
ADD COLUMN status VARCHAR(20) NOT NULL DEFAULT 'ACTIVE';
