-- Toda la tarea esta dentro de la carpeta 4

-- 1.Obtenga todos los libros y sus autores (en caso de tenerlos)
SELECT b.id, b.name AS 'Book Name', a.id, a.name AS 'Author Name'
FROM books b
LEFT JOIN authors  a on a.id = b.author_id;

-- 2. Obtenga todos los libros que no tienen autor
SELECT *
FROM books b
WHERE b.author_id IS NULL;

-- 3. Obtenga todos los autores que no tienen libros
SELECT a.id, a.name
FROM books b
RIGHT JOIN authors a ON b.author_id = a.id
WHERE b.author_id IS NULL;

-- Obtenga todos los libros que han sido rentados en algún momento
SELECT b.id, b.name
FROM rents r
JOIN books b ON r.book_id = b.id
GROUP BY b.id;

-- Obtenga todos los libros que nunca han sido rentados
SELECT b.id, b.name
FROM rents r
RIGHT JOIN books b ON b.id = r.book_id
WHERE r.id IS NULL;

-- Obtenga todos los clientes que nunca han rentado un libro
SELECT c.id, c.name
FROM rents r
RIGHT JOIN customers c ON r.customer_id = c.id
WHERE r.id IS NULL;

-- Obtenga todos los libros que han sido rentados y están en estado “Overdue”
SELECT *
FROM rents r
JOIN books b ON b.id = r.book_id
WHERE LOWER(state) = 'overdue';
