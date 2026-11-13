-- Link del diagrama https://drawsql.app/teams/alejandro-solano/diagrams/ejericio-3-normalizacion-cars


CREATE TABLE `cars`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `model_id` BIGINT NOT NULL,
    `color_id` BIGINT NOT NULL,
    `vin` VARCHAR(255) NOT NULL
);
ALTER TABLE
    `cars` ADD UNIQUE `cars_vin_unique`(`vin`);
CREATE TABLE `makes`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL
);
CREATE TABLE `models`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL,
    `make_id` BIGINT NOT NULL,
    `year_id` BIGINT NOT NULL
);
CREATE TABLE `years`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `year` INT NOT NULL
);
CREATE TABLE `colors`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `description` VARCHAR(255) NOT NULL
);
CREATE TABLE `owners`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL
);
CREATE TABLE `phones`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `phone` VARCHAR(255) NOT NULL,
    `owner_id` BIGINT NOT NULL
);
CREATE TABLE `insurance_companies`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL
);
CREATE TABLE `insurance_policies`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL,
    `description` VARCHAR(255) NOT NULL,
    `insurance_company_id` BIGINT NOT NULL
);
CREATE TABLE `car_insurance_policy`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `car_id` BIGINT NOT NULL,
    `insurance_policy_id` BIGINT NOT NULL
);
CREATE TABLE `car_owner`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `owner_id` BIGINT NOT NULL,
    `car_id` BIGINT NOT NULL
);
ALTER TABLE
    `insurance_policies` ADD CONSTRAINT `insurance_policies_insurance_company_id_foreign` FOREIGN KEY(`insurance_company_id`) REFERENCES `insurance_companies`(`id`);
ALTER TABLE
    `car_insurance_policy` ADD CONSTRAINT `car_insurance_policy_insurance_policy_id_foreign` FOREIGN KEY(`insurance_policy_id`) REFERENCES `insurance_policies`(`id`);
ALTER TABLE
    `models` ADD CONSTRAINT `models_year_id_foreign` FOREIGN KEY(`year_id`) REFERENCES `years`(`id`);
ALTER TABLE
    `phones` ADD CONSTRAINT `phones_owner_id_foreign` FOREIGN KEY(`owner_id`) REFERENCES `owners`(`id`);
ALTER TABLE
    `cars` ADD CONSTRAINT `cars_color_id_foreign` FOREIGN KEY(`color_id`) REFERENCES `colors`(`id`);
ALTER TABLE
    `car_insurance_policy` ADD CONSTRAINT `car_insurance_policy_car_id_foreign` FOREIGN KEY(`car_id`) REFERENCES `cars`(`id`);
ALTER TABLE
    `models` ADD CONSTRAINT `models_make_id_foreign` FOREIGN KEY(`make_id`) REFERENCES `makes`(`id`);
ALTER TABLE
    `car_owner` ADD CONSTRAINT `car_owner_car_id_foreign` FOREIGN KEY(`car_id`) REFERENCES `cars`(`id`);
ALTER TABLE
    `car_owner` ADD CONSTRAINT `car_owner_owner_id_foreign` FOREIGN KEY(`owner_id`) REFERENCES `owners`(`id`);
ALTER TABLE
    `cars` ADD CONSTRAINT `cars_model_id_foreign` FOREIGN KEY(`model_id`) REFERENCES `models`(`id`);