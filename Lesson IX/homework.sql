CREATE DATABASE IF NOT EXISTS company_employees;
USE company_employees;
CREATE TABLE IF NOT EXISTS employees (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT primary key,
	first_name VARCHAR(30) NOT NULL,
last_name VARCHAR(30) NOT NULL
);
INSERT INTO employees (id, first_name, last_name) VALUES (null, 'Ivan', 'Ivanov');
INSERT INTO employees (id, first_name, last_name) VALUES (null, 'Petr', 'Petrov');
INSERT INTO employees (id, first_name, last_name) VALUES (null, 'Sergey', 'Sergeev');
INSERT INTO employees (id, first_name, last_name) VALUES (null, 'Nikita', 'Nikitin');
INSERT INTO employees (id, first_name, last_name) VALUES (null, 'Maksim', 'Maksimov');
INSERT INTO employees (id, first_name, last_name) VALUES (null, 'Aleksey','Alekseev');
INSERT INTO employees (id, first_name, last_name) VALUES (null, 'Fedor', 'Fedorov');
CREATE TABLE IF NOT EXISTS positions (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT primary key, 
	position_name VARCHAR(30) NOT NULL,
salary_RUB DECIMAL(10) NOT NULL   
);
INSERT INTO positions (id, position_name, salary_RUB) VALUES (null, 'director ', 100000);
INSERT INTO positions (id, position_name, salary_RUB) VALUES (null, 'foreman', 50000);
INSERT INTO positions (id, position_name, salary_RUB) VALUES (null, 'senior electrician', 28000);
INSERT INTO positions (id, position_name, salary_RUB) VALUES (null, 'electrician', 25000);
ALTER TABLE employees ADD position_id INTEGER NOT NULL;
UPDATE employees SET position_id=1 WHERE id=1;
UPDATE employees SET position_id=2 WHERE id IN (2,3);
UPDATE employees SET position_id=3 WHERE id IN (4,5);
UPDATE employees SET position_id=4 WHERE id IN (6,7);
SELECT employee.first_name, employee.last_name, position.position_name, position.salary_RUB 
FROM employees employee
INNER JOIN positions position ON employee.position_id = position.id WHERE position.salary_RUB < 30000;
SELECT employee.first_name, employee.last_name, position.position_name, position.salary_RUB 
FROM employees employee
INNER JOIN positions position ON employee.position_id = position.id WHERE (position. position_name = 'electrician') and (position.salary_RUB < 30000);
