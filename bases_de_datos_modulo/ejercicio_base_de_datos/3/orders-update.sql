-- Link del diagrama: https://drawsql.app/teams/alejandro-solano/diagrams/ejercicio-1-normalizacion
CREATE TABLE `customers`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL,
    `last_name` VARCHAR(255) NOT NULL
);
CREATE TABLE `phones`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `phone` TEXT NOT NULL,
    `customer_id` BIGINT NOT NULL
);
CREATE TABLE `addresses`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `country` VARCHAR(255) NOT NULL,
    `province` VARCHAR(255) NOT NULL,
    `address` VARCHAR(255) NOT NULL,
    `customer_id` BIGINT NOT NULL
);
CREATE TABLE `orders`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `delivery_time` DATETIME NOT NULL,
    `total_amount` DECIMAL(8, 2) NOT NULL,
    `address_id` BIGINT NOT NULL
);
CREATE TABLE `items`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL,
    `price` DECIMAL(8, 2) NOT NULL,
    `stock` BIGINT NOT NULL
);
CREATE TABLE `order_item`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `order_id` BIGINT NOT NULL,
    `item_id` BIGINT NOT NULL,
    `item_quantity` BIGINT NOT NULL
);
CREATE TABLE `special_requests`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `description` VARCHAR(255) NOT NULL,
    `order_item_id` BIGINT NOT NULL
);
ALTER TABLE
    `order_item` ADD CONSTRAINT `order_item_order_id_foreign` FOREIGN KEY(`order_id`) REFERENCES `orders`(`id`);
ALTER TABLE
    `special_requests` ADD CONSTRAINT `special_requests_order_item_id_foreign` FOREIGN KEY(`order_item_id`) REFERENCES `order_item`(`id`);
ALTER TABLE
    `addresses` ADD CONSTRAINT `addresses_id_foreign` FOREIGN KEY(`id`) REFERENCES `orders`(`address_id`);
ALTER TABLE
    `addresses` ADD CONSTRAINT `addresses_customer_id_foreign` FOREIGN KEY(`customer_id`) REFERENCES `customers`(`id`);
ALTER TABLE
    `order_item` ADD CONSTRAINT `order_item_item_id_foreign` FOREIGN KEY(`item_id`) REFERENCES `items`(`id`);
ALTER TABLE
    `phones` ADD CONSTRAINT `phones_customer_id_foreign` FOREIGN KEY(`customer_id`) REFERENCES `customers`(`id`);