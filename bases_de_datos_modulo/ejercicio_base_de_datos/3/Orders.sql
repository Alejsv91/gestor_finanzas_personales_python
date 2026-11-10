
-- 1. Se creó la tabla `customers` aplicando la Primera y Segunda Forma Normal (1FN y 2FN) 
--    para aislar las entidades y eliminar por completo la redundancia de datos.
-- 2. Las entidades `phones` y `addresses` se desglosaron en tablas independientes 
--    con una relación de 1:N hacia `customers` mediante llaves foráneas (`customer_id`), 
--    permitiendo que un cliente tenga múltiples métodos de contacto o direcciones de envío.
-- 3. La tabla `orders` mapea las transacciones vinculando directamente el `customer_id` 
--    y el `address_id` correspondiente a la entrega, asegurando la integridad referencial.
-- 4. Para resolver la relación de Muchos a Muchos (M:N) entre `orders` e `items`, se 
--    diseñó la tabla asociativa `order_item` (tabla de rompimiento), la cual registra el 
--    historial, cantidades (`item_quantity`) y desglosa los artículos por cada orden.
-- 5. Finalmente, la tabla `special_requests` extiende los detalles específicos de cada 
--    artículo solicitado en una relación 1:N con la tabla asociativa `order_item`.

-- En este link puedes ver el diagrama
-- https://drawsql.app/teams/alejandro-solano/diagrams/ejercicio-1-normalizacion


CREATE TABLE `customers`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL,
    `last_name` VARCHAR(255) NOT NULL
);

CREATE TABLE `phones`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `phone` VARCHAR(50) NOT NULL,
    `customer_id` BIGINT UNSIGNED NOT NULL
);

CREATE TABLE `addresses`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `country` VARCHAR(255) NOT NULL,
    `province` VARCHAR(255) NOT NULL,
    `address` VARCHAR(255) NOT NULL,
    `customer_id` BIGINT UNSIGNED NOT NULL
);

CREATE TABLE `orders`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `delivery_time` DATETIME NOT NULL,
    `total_amount` DECIMAL(8, 2) NOT NULL,
    `customer_id` BIGINT UNSIGNED NOT NULL,
    `address_id` BIGINT UNSIGNED NOT NULL
);

CREATE TABLE `items`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL,
    `price` DECIMAL(8, 2) NOT NULL,
    `stock` BIGINT UNSIGNED NOT NULL
);

CREATE TABLE `order_item`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `order_id` BIGINT UNSIGNED NOT NULL,
    `item_id` BIGINT UNSIGNED NOT NULL,
    `item_quantity` BIGINT UNSIGNED NOT NULL
);

CREATE TABLE `special_requests`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `description` VARCHAR(255) NOT NULL,
    `order_item_id` BIGINT UNSIGNED NOT NULL
);

ALTER TABLE `phones` 
    ADD CONSTRAINT `phones_customer_id_foreign` 
    FOREIGN KEY(`customer_id`) REFERENCES `customers`(`id`) ON DELETE CASCADE;

ALTER TABLE `addresses` 
    ADD CONSTRAINT `addresses_customer_id_foreign` 
    FOREIGN KEY(`customer_id`) REFERENCES `customers`(`id`) ON DELETE CASCADE;

ALTER TABLE `orders` 
    ADD CONSTRAINT `orders_customer_id_foreign` 
    FOREIGN KEY(`customer_id`) REFERENCES `customers`(`id`);

ALTER TABLE `orders` 
    ADD CONSTRAINT `orders_address_id_foreign` 
    FOREIGN KEY(`address_id`) REFERENCES `addresses`(`id`);

ALTER TABLE `order_item` 
    ADD CONSTRAINT `order_item_order_id_foreign` 
    FOREIGN KEY(`order_id`) REFERENCES `orders`(`id`) ON DELETE CASCADE;

ALTER TABLE `order_item` 
    ADD CONSTRAINT `order_item_item_id_foreign` 
    FOREIGN KEY(`item_id`) REFERENCES `items`(`id`);

ALTER TABLE `special_requests` 
    ADD CONSTRAINT `special_requests_order_item_id_foreign` 
    FOREIGN KEY(`order_item_id`) REFERENCES `order_item`(`id`) ON DELETE CASCADE;
