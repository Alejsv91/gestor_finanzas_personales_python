-- Puedes ver el diagrama aqui: https://drawsql.app/teams/alejandro-solano/diagrams/ejercicio-extra-normalizacion-empleados-y-proyectos

-- 1FN
-- - Los valores ya son atómicos (no hay listas en una celda). Solo se define la PK compuesta (employee_id, project_id), porque un empleado puede estar en varios proyectos.

-- 2FN
-- - Había dependencias parciales: employee_name, department y department_phone dependen solo de employee_id; project_name y project_budget dependen solo de project_id.
-- - Se separa en: employees(employee_id, name, department, department_phone), projects(project_id, name, budget) y employee_project(employee_id, project_id).
-- - Así el nombre de Ana ya no se repite por cada proyecto.

-- 3FN
-- - En employees había una dependencia transitiva: employee_id → department → department_phone. El teléfono depende del departamento, no del empleado.
-- - Se separa en: departments(id, name, phone) y employees(id, name, department_id).
-- - Si cambia el teléfono de IT, se actualiza en un solo lugar.

-- Resultado final
-- - departments, employees, projects y employee_project, relacionadas por llaves foráneas (employees.department_id y employee_project).


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