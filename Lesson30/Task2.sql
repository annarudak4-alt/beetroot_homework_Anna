--Відображення імен (ім'я, прізвище) з псевдонімами
SELECT 
    first_name AS "Ім'я",
    last_name AS "Прізвище"
FROM employees;

--Отримання унікальних ідентифікаторів відділів
SELECT DISTINCT department_id
FROM employees;

--Всі дані співробітників, відсортовані за ім'ям у порядку спадання
SELECT *
FROM employees
ORDER BY first_name DESC;

--Ім'я, прізвище, зарплата та пенсійний фонд (12% від зарплати)
SELECT 
    first_name,
    last_name,
    salary,
    salary * 0.12 AS pension_fund
FROM employees;

--Максимальна та мінімальна зарплата
SELECT 
    MAX(salary) AS max_salary,
    MIN(salary) AS min_salary
FROM employees;

--Місячна зарплата (округлена до двох знаків)
SELECT 
    first_name,
    last_name,
    ROUND(salary / 12.0, 2) AS monthly_salary
FROM employees;