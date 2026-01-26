-- 1. Відображення імені, прізвища, номера відділу та назви відділу для кожного співробітника
SELECT
    e.first_name,
    e.last_name,
    e.department_id,
    d.depart_name
FROM
    employees AS e
JOIN
    departments AS d ON e.department_id = d.department_id;

-- 2. Відображення імені та прізвища, відділу, міста та штату/області для кожного співробітника.
SELECT
    e.first_name,
    e.last_name,
    d.depart_name AS department_name,
    l.city,
    l.state_province
FROM
    employees AS e
JOIN
    departments AS d ON e.department_id = d.department_id
JOIN
    locations AS l ON d.location_id = l.location_id;

-- 3. Відображення імені, прізвища, номера відділу та назви відділу для всіх співробітників відділів 80 або 40.
SELECT
    e.first_name,
    e.last_name,
    e.department_id,
    d.depart_name
FROM
    employees AS e
JOIN
    departments AS d ON e.department_id = d.department_id
WHERE
    e.department_id IN (80, 40);

-- 4. Відображення всіх відділів, включаючи ті, де немає жодного співробітника (використовуємо LEFT JOIN, щоб зберегти всі відділи).
SELECT
    d.depart_name,
    d.department_id,
    e.first_name,
    e.last_name
FROM
    departments AS d
LEFT JOIN
    employees AS e ON d.department_id = e.department_id;

-- 5. Виведення імен усіх співробітників, включаючи ім'я їхнього керівника (використовуємо self-join).
SELECT
    e.first_name || ' ' || e.last_name AS employee_full_name,
    m.first_name || ' ' || m.last_name AS manager_full_name
FROM
    employees AS e
LEFT JOIN
    employees AS m ON e.manager_id = m.employee_id;

-- 6. Вивести посаду, повне ім'я (ім'я та прізвище) працівника та різницю між максимальною зарплатою для посади та зарплатою працівника.
SELECT
    j.job_title,
    e.first_name || ' ' || e.last_name AS employee_full_name,
    j.max_salary - e.salary AS salary_difference
FROM
    employees AS e
JOIN
    jobs AS j ON e.job_id = j.job_id;

-- 7. Відображення посади та середньої зарплати співробітників.
SELECT
    j.job_title,
    AVG(e.salary) AS average_salary
FROM
    employees AS e
JOIN
    jobs AS j ON e.job_id = j.job_id
GROUP BY
    j.job_title;

-- 8. Відображення повного імені (ім'я та прізвище) та зарплати тих співробітників, які працюють у будь-якому відділі, розташованому в Лондоні.
SELECT
    e.first_name || ' ' || e.last_name AS employee_full_name,
    e.salary
FROM
    employees AS e
JOIN
    departments AS d ON e.department_id = d.department_id
JOIN
    locations AS l ON d.location_id = l.location_id
WHERE
    l.city = 'London';

-- 9. Відображення назви відділу та кількості співробітників у кожному відділі (включаючи відділи без співробітників).
SELECT
    d.depart_name,
    COUNT(e.employee_id) AS number_of_employees
FROM
    departments AS d
LEFT JOIN
    employees AS e ON d.department_id = e.department_id
GROUP BY
    d.depart_name
ORDER BY
    number_of_employees DESC;