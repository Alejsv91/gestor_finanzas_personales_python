-- SQLite
-- sqlite no soport numeric o decimal, consulte a la IA 
-- y me recomendo agregarlo como integer y que se maneja como centavos
-- Con date me recomendo dejarlo como texto

CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code VARCHAR(255) UNIQUE NOT NULL,
    price INTEGER NOT NULL,
    entry_date TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL,
    brand VARCHAR(40) NOT NULL,
    stock_available INTEGER NOT NULL,
    name VARCHAR(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS shopping_carts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    buyer_email varchar(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS shopping_cart_product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    shopping_cart_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    total_amount INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (shopping_cart_id) REFERENCES shopping_carts(id)
);

CREATE TABLE IF NOT EXISTS invoices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_number INTEGER UNIQUE NOT NULL,
    purchase_date TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL,
    buyer_email varchar(50) NOT NULL,
    total_amount INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS product_per_invoice (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    invoice_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    total_amount INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (invoice_id) REFERENCES invoices(id)
);

-- ALTER TABLE invoices ADD COLUMN user_phone_number TEXT;
-- ALTER TABLE invoices ADD COLUMN employee_code TEXT;

