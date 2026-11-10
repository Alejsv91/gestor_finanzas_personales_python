-- Diagrama aquí: https://drawsql.app/teams/alejandro-solano/diagrams/registro-de-clases

-- 1FN
-- - Los valores ya son atómicos (no hay listas en una celda). 

-- 2FN
-- - Había dependencias parciales: student_name depende solo de student_id; course_name, instructor_name e instructor_email dependen solo de course_code.
-- - Se separa en: students(student_id, name), courses(course_code, name, instructor_name, instructor_email) y student_course(student_id, course_code).
-- - Así el nombre de Marco ya no se repite por cada curso, ni el nombre de Python I por cada estudiante.

-- 3FN
-- - En courses había una dependencia transitiva: course_code → instructor_name → instructor_email. El email depende del instructor, no del curso.
-- - Se separa en: instructors(id, name, email) y courses(id, code, name, instructor_id).
-- - Si cambia el email de Juan Pérez, se actualiza en un solo lugar.

-- Resultado final
-- - students, courses, instructors y student_course, relacionadas por llaves foráneas (courses.instructor_id, student_course.student_id y student_course.course_id).

CREATE TABLE `students`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL
);
CREATE TABLE `courses`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `code` BIGINT NOT NULL,
    `name` VARCHAR(255) NOT NULL,
    `instructor_id` BIGINT NOT NULL
);
CREATE TABLE `student_course`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `student_id` BIGINT NOT NULL,
    `course_id` BIGINT NOT NULL
);
CREATE TABLE `instructors`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL,
    `email` VARCHAR(255) NOT NULL
);
ALTER TABLE
    `student_course` ADD CONSTRAINT `student_course_course_id_foreign` FOREIGN KEY(`course_id`) REFERENCES `courses`(`id`);
ALTER TABLE
    `student_course` ADD CONSTRAINT `student_course_student_id_foreign` FOREIGN KEY(`student_id`) REFERENCES `students`(`id`);
ALTER TABLE
    `courses` ADD CONSTRAINT `courses_instructor_id_foreign` FOREIGN KEY(`instructor_id`) REFERENCES `instructors`(`id`);