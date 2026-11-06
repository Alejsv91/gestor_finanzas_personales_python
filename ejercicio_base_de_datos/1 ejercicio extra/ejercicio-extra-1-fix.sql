CREATE TABLE `products`(
    `id` BIGINT NOT NULL,
    `code` VARCHAR(255) NOT NULL,
    `price` DOUBLE NOT NULL,
    `entry_date` DATE NOT NULL,
    `brand` VARCHAR(255) NOT NULL,
    `stock_available` INT NOT NULL,
    `name` VARCHAR(255) NOT NULL,
    PRIMARY KEY(`id`)
);
ALTER TABLE
    `products` ADD UNIQUE `products_code_unique`(`code`);
CREATE TABLE `invoices`(
    `id` BIGINT NOT NULL,
    `invoice_number` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `purchase_date` DATETIME NOT NULL,
    `total_amount` FLOAT(53) NOT NULL,
    `user_id` BIGINT NOT NULL,
    `payment_method_id` BIGINT NOT NULL,
    PRIMARY KEY(`id`)
);
CREATE TABLE `shopping_carts`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `buyer_email` VARCHAR(255) NOT NULL
);
CREATE TABLE `products_per_invoice`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `product_id` BIGINT NOT NULL,
    `invoice_id` BIGINT NOT NULL,
    `quantity` INT NOT NULL,
    `total_amount` FLOAT(53) NOT NULL
);
CREATE TABLE `shopping_cart_product`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `product_id` BIGINT NOT NULL,
    `shopping_cart_id` VARCHAR(255) NOT NULL,
    `quantity` BIGINT NOT NULL,
    `total_amount` FLOAT(53) NOT NULL
);
CREATE TABLE `users`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `full_name` VARCHAR(255) NOT NULL,
    `email` VARCHAR(255) NOT NULL,
    `registration_date` DATETIME NOT NULL
);
ALTER TABLE
    `users` ADD UNIQUE `users_email_unique`(`email`);
CREATE TABLE `reviews`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `product_id` VARCHAR(255) NOT NULL,
    `comment` VARCHAR(255) NOT NULL,
    `rating` INT NOT NULL,
    `date` DATE NOT NULL,
    `user_id` BIGINT NOT NULL
);
CREATE TABLE `payment_methods`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `method_type` VARCHAR(255) NOT NULL,
    `bank_name` VARCHAR(255) NOT NULL
);
CREATE TABLE `invoice_payment_method`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `invoice_id` BIGINT NOT NULL,
    `payment_method_id` BIGINT NOT NULL
);
ALTER TABLE
    `invoices` ADD CONSTRAINT `invoices_user_id_foreign` FOREIGN KEY(`user_id`) REFERENCES `users`(`id`);
ALTER TABLE
    `invoices` ADD CONSTRAINT `invoices_id_foreign` FOREIGN KEY(`id`) REFERENCES `products_per_invoice`(`invoice_id`);
ALTER TABLE
    `products` ADD CONSTRAINT `products_id_foreign` FOREIGN KEY(`id`) REFERENCES `products_per_invoice`(`product_id`);
ALTER TABLE
    `reviews` ADD CONSTRAINT `reviews_product_id_foreign` FOREIGN KEY(`product_id`) REFERENCES `products`(`id`);
ALTER TABLE
    `shopping_cart_product` ADD CONSTRAINT `shopping_cart_product_shopping_cart_id_foreign` FOREIGN KEY(`shopping_cart_id`) REFERENCES `shopping_carts`(`id`);
ALTER TABLE
    `reviews` ADD CONSTRAINT `reviews_user_id_foreign` FOREIGN KEY(`user_id`) REFERENCES `users`(`id`);
ALTER TABLE
    `invoice_payment_method` ADD CONSTRAINT `invoice_payment_method_payment_method_id_foreign` FOREIGN KEY(`payment_method_id`) REFERENCES `payment_methods`(`id`);
ALTER TABLE
    `invoice_payment_method` ADD CONSTRAINT `invoice_payment_method_invoice_id_foreign` FOREIGN KEY(`invoice_id`) REFERENCES `invoices`(`id`);
ALTER TABLE
    `shopping_cart_product` ADD CONSTRAINT `shopping_cart_product_product_id_foreign` FOREIGN KEY(`product_id`) REFERENCES `products`(`id`);