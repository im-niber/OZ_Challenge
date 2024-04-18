CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(100),
    salary DECIMAL(10, 2)
);

INSERT INTO employees (name, position, salary) VALUES ('혜린', 'PM', 90000);
INSERT INTO employees (name, position, salary) VALUES ('은우', 'Frontend', 80000);
INSERT INTO employees (name, position, salary) VALUES ('가을', 'Backend', 92000);
INSERT INTO employees (name, position, salary) VALUES ('지수', 'Frontend', 78000);
INSERT INTO employees (name, position, salary) VALUES ('민혁', 'Frontend', 96000);
INSERT INTO employees (name, position, salary) VALUES ('하온', 'Backend', 130000);

SELECT * FROM employees;

SELECT name, salary FROM employees WHERE position = 'Frontend' AND salary <= 90000;

UPDATE employees SET salary = salary * 1.10 WHERE position = 'PM';
SELECT * FROM employees WHERE position = 'PM';

UPDATE employees SET salary = salary * 1.05 WHERE position = 'Backend';

DELETE FROM employees WHERE name = '민혁';

SELECT position, AVG(salary) AS average FROM employees GROUP BY position;

DROP TABLE employees;