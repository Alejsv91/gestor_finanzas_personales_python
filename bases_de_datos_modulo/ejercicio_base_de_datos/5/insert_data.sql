-- SCHEMA: store_db

-- DROP SCHEMA IF EXISTS store_db ;

CREATE SCHEMA IF NOT EXISTS store_db
    AUTHORIZATION alejandrosolanovega;

SET search_path TO store_db;

-- 1. Insertar usuarios
INSERT INTO users (name, last_name, email) VALUES
('Alejandro', 'Solano', 'alejandro.solano@correo.com'),
('María', 'Fernández', 'maria.fernandez@correo.com'),
('Carlos', 'Ramírez', 'carlos.ramirez@correo.com'),
('Laura', 'Jiménez', 'laura.jimenez@correo.com');

-- 2. Insertar productos (todos con stock disponible > 0)
INSERT INTO products (code, name, stock, price) VALUES
('PROD-001', 'Laptop Dell Inspiron 15', 15, 750.00),
('PROD-002', 'Mouse Inalámbrico Logitech', 45, 25.50),
('PROD-003', 'Teclado Mecánico RGB', 20, 65.00),
('PROD-004', 'Monitor Samsung 24 pulgadas', 10, 180.00),
('PROD-005', 'Audífonos Bluetooth Sony', 30, 89.99);

-- 3. Insertar facturas (vinculadas a los usuarios con IDs 1, 2 y 3)
INSERT INTO bills (date, user_id, total) VALUES
('2026-11-15 10:30:00', 1, 801.00),
('2026-11-16 14:15:00', 2, 154.99),
('2026-11-16 18:45:00', 3, 360.00),
('2026-11-17 09:20:00', 1, 256.48);

-- 4. Insertar detalle de productos por factura
INSERT INTO product_bill (product_id, quantity, bill_id, unit_price) VALUES
-- Detalle Factura 1 (1 Laptop + 2 Mouse = 750.00 + 51.00 = 801.00)
(1, 1, 1, 750.00),
(2, 2, 1, 25.50),

-- Detalle Factura 2 (1 Teclado + 1 Audífonos = 65.00 + 89.99 = 154.99)
(3, 1, 2, 65.00),
(5, 1, 2, 89.99),

-- Detalle Factura 3 (2 Monitores = 360.00)
(4, 2, 3, 180.00),

-- Detalle Factura 4 (3 Mouse + 2 Audífonos = 76.50 + 179.98 = 256.48)
(2, 3, 4, 25.50),
(5, 2, 4, 89.99);



