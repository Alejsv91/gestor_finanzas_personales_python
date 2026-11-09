-- SQLite
-- 1. Obtener todos los productos almacenados
SELECT *
FROM products;

-- 2. Obtener todos los productos que tengan un precio mayor a 50000
SELECT *
FROM products
WHERE price > 5000000;

-- 3. Obtenga todas las compras de un mismo producto por id
SELECT *
from product_per_invoice pi
INNER JOIN products p on p.id = pi.product_id
INNER JOIN invoices i on i.id = pi.invoice_id
WHERE pi.product_id = 1;

-- 4. Obtenga todas las compras agrupadas por producto, 
-- donde se muestre el total comprado entre todas las compras.
SELECT  SUM(pi.total_amount), COUNT(*), p.id, p.name
FROM product_per_invoice pi
INNER JOIN products p on p.id = pi.product_id
INNER JOIN invoices i on i.id = pi.invoice_id
GROUP BY pi.product_id;

-- 5. Obtenga todas las facturas realizadas por el mismo comprador
SELECT *
FROM product_per_invoice pi
INNER JOIN products p on p.id = pi.product_id
INNER JOIN invoices i on i.id = pi.invoice_id
WHERE i.buyer_email = 'juan.perez@email.com';

-- 6. Obtenga todas las facturas ordenadas por monto total de forma 
-- descendente
SELECT * 
FROM invoices
ORDER BY total_amount DESC;

-- 7. Obtenga una sola factura por número de factura.
SELECT *
FROM invoices i
WHERE i.invoice_number = 1001;