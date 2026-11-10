-- Puedes ver el diagrama aqui: 

CREATE TABLE `employees`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL,
    `last_name` VARCHAR(255) NOT NULL,
    `department_id` BIGINT NOT NULL
);
CREATE TABLE `departments`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL
);
CREATE TABLE `projects`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL,
    `budget` DECIMAL(8, 2) NOT NULL
);
CREATE TABLE `department_project`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `employee_id` BIGINT NOT NULL,
    `project_id` BIGINT NOT NULL
);
ALTER TABLE
    `department_project` ADD UNIQUE `department_project_employee_id_unique`(`employee_id`);
ALTER TABLE
    `department_project` ADD UNIQUE `department_project_project_id_unique`(`project_id`);
CREATE TABLE `department_phones`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `phone` TEXT NOT NULL,
    `department_id` BIGINT NOT NULL
);
ALTER TABLE
    `employees` ADD CONSTRAINT `employees_department_id_foreign` FOREIGN KEY(`department_id`) REFERENCES `departments`(`id`);
ALTER TABLE
    `department_phones` ADD CONSTRAINT `department_phones_department_id_foreign` FOREIGN KEY(`department_id`) REFERENCES `departments`(`id`);
ALTER TABLE
    `department_project` ADD CONSTRAINT `department_project_project_id_foreign` FOREIGN KEY(`project_id`) REFERENCES `projects`(`id`);
ALTER TABLE
    `department_project` ADD CONSTRAINT `department_project_employee_id_foreign` FOREIGN KEY(`employee_id`) REFERENCES `employees`(`id`);