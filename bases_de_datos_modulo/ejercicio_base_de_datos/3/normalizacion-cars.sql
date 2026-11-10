-- Principio general: cada entidad tiene su propia tabla para que cada dato se guarde una sola vez 
-- (1FN: valores atómicos; 2FN: sin dependencias parciales; 3FN: sin dependencias transitivas). Las relaciones se hacen con llaves foráneas.
-- •	makes: guarda las marcas una sola vez, sin repetirlas en cada auto.
-- •	models: guarda los modelos con make_id; la marca depende del modelo, no del auto (evita dependencia transitiva).
-- •	years / colors: catálogos que evitan repetir y escribir de forma inconsistente los mismos valores.
-- •	owners: datos del dueño; un dueño puede tener varios autos, así que no se repiten en cars.
-- •	phones: un dueño puede tener varios teléfonos; una fila por teléfono respeta la 1FN (valores atómicos).
-- •	cars: tabla central; solo contiene su id y las llaves foráneas a modelo, año, color y dueño.
-- •	insurance_companies: guarda cada aseguradora una sola vez.
-- •	insurance_policies: guarda las pólizas con insurance_company_id; la póliza depende de la aseguradora, no del auto.
-- •	car_insurance_policies: tabla intermedia para la relación muchos a muchos entre autos y pólizas, evitando listas en una celda (1FN).

-- En este link puedes ver el diagrama
-- https://drawsql.app/teams/alejandro-solano/diagrams/ejericio-3-normalizacion-cars 


CREATE TABLE `cars`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `model_id` BIGINT NOT NULL,
    `year_id` BIGINT NOT NULL,
    `color_id` BIGINT NOT NULL,
    `owner_id` BIGINT NOT NULL
);
CREATE TABLE `makes`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL
);
CREATE TABLE `models`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL,
    `model_id` BIGINT NOT NULL
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
ALTER TABLE
    `insurance_policies` ADD CONSTRAINT `insurance_policies_insurance_company_id_foreign` FOREIGN KEY(`insurance_company_id`) REFERENCES `insurance_companies`(`id`);
ALTER TABLE
    `car_insurance_policy` ADD CONSTRAINT `car_insurance_policy_insurance_policy_id_foreign` FOREIGN KEY(`insurance_policy_id`) REFERENCES `insurance_policies`(`id`);
ALTER TABLE
    `phones` ADD CONSTRAINT `phones_owner_id_foreign` FOREIGN KEY(`owner_id`) REFERENCES `owners`(`id`);
ALTER TABLE
    `cars` ADD CONSTRAINT `cars_color_id_foreign` FOREIGN KEY(`color_id`) REFERENCES `colors`(`id`);
ALTER TABLE
    `car_insurance_policy` ADD CONSTRAINT `car_insurance_policy_car_id_foreign` FOREIGN KEY(`car_id`) REFERENCES `cars`(`id`);
ALTER TABLE
    `models` ADD CONSTRAINT `models_model_id_foreign` FOREIGN KEY(`model_id`) REFERENCES `makes`(`id`);
ALTER TABLE
    `cars` ADD CONSTRAINT `cars_owner_id_foreign` FOREIGN KEY(`owner_id`) REFERENCES `owners`(`id`);
ALTER TABLE
    `cars` ADD CONSTRAINT `cars_model_id_foreign` FOREIGN KEY(`model_id`) REFERENCES `models`(`id`);
ALTER TABLE
    `cars` ADD CONSTRAINT `cars_year_id_foreign` FOREIGN KEY(`year_id`) REFERENCES `years`(`id`);