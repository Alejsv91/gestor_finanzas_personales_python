-- Diagrama aquí: https://drawsql.app/teams/alejandro-solano/diagrams/hospital-citas-medicas

CREATE TABLE `patients`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL
);
CREATE TABLE `phones`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `phone` TEXT NOT NULL,
    `patient_id` BIGINT NOT NULL
);
CREATE TABLE `doctors`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL
);
CREATE TABLE `specialties`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL
);
CREATE TABLE `doctor_speciality`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `speciality_id` BIGINT NOT NULL,
    `doctor_id` BIGINT NOT NULL
);
CREATE TABLE `appointments`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `date` DATE NOT NULL,
    `time` TIME NOT NULL,
    `description` VARCHAR(255) NOT NULL,
    `patient_id` BIGINT NOT NULL,
    `doctor_id` BIGINT NOT NULL
);
ALTER TABLE
    `phones` ADD CONSTRAINT `phones_patient_id_foreign` FOREIGN KEY(`patient_id`) REFERENCES `patients`(`id`);
ALTER TABLE
    `doctor_speciality` ADD CONSTRAINT `doctor_speciality_speciality_id_foreign` FOREIGN KEY(`speciality_id`) REFERENCES `specialties`(`id`);
ALTER TABLE
    `appointments` ADD CONSTRAINT `appointments_doctor_id_foreign` FOREIGN KEY(`doctor_id`) REFERENCES `doctors`(`id`);
ALTER TABLE
    `appointments` ADD CONSTRAINT `appointments_id_foreign` FOREIGN KEY(`id`) REFERENCES `patients`(`id`);
ALTER TABLE
    `doctor_speciality` ADD CONSTRAINT `doctor_speciality_doctor_id_foreign` FOREIGN KEY(`doctor_id`) REFERENCES `doctors`(`id`);