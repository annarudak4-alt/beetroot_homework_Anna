--Створення таблиці
CREATE TABLE measuring_technique (
  id INTEGER PRIMARY KEY,
  name TEXT,
  department TEXT
);

--Перейменування таблиці
ALTER TABLE measuring_technique RENAME TO measuring_equipment;

--Додавання нового стовпця
ALTER TABLE measuring_equipment ADD COLUMN date_of_inspection TEXT;

--Вставка рядків
INSERT INTO measuring_equipment (id, name, department, date_of_inspection)
VALUES (1, 'stethoscope', 'Wheel-roller', '2025-10-21');

INSERT INTO measuring_equipment (id, name, department, date_of_inspection)
VALUES (2, 'caliber', 'Trolley', '2025-08-21');

INSERT INTO measuring_equipment (id, name, department, date_of_inspection)
VALUES (3, 'template', 'Braking', '2025-09-21');

--Оновити рядок
UPDATE measuring_equipment 
SET date_of_inspection='control' 
WHERE name='stethoscope';

--Видалення рядка
DELETE FROM measuring_equipment 
WHERE name='template';
