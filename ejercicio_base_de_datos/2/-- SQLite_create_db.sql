-- SQLite
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name varchar(200)  NOT NULL,
    email varchar(255) UNIQUE NOT NULL,
    registration_date NOT NULL DEFAULT (datetime('now', 'localtime'))
)

CREATE TABLE IF NOT EXISTS payment_method (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    method_type varchar(40) NOT NULL,
    bank_name varchar(40) NOT NULL
)

CREATE TABLE IF NOT EXISTS invoices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_number BIGINT UNIQUE NOT NULL,
    purchase_date (datetime('now', 'localtime')),
    total_amount FLOAT,
    user_id INTEGER,
    payment_method INTEGER, 
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (payment_method_id) REFERENCES payment_method(id)
    )





