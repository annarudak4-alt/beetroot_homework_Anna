"""Task 1
 
 Школа
Створіть структуру класів на Python, яка представляє людей у школі.
Створіть базовий клас під назвою Person, клас під назвою Student та
ще один під назвою Teacher. Спробуйте знайти якомога більше методів
та атрибутів, які належать до різних класів, і пам'ятайте, які з них
є спільними, а які ні. Наприклад, ім'я має бути атрибутом Person, тоді
як зарплата має бути доступною лише вчителю.
"""
class Person:
    def __init__(self, name, status=''):
        self.name = name
        self.status = status

    def info(self):
        raise NotImplementedError("Subclasses must implement info()")

class Teacher(Person):
    def __init__(self, name, salary, subject, group):
        super().__init__(name)
        self.salary = salary
        self.subjects = [subject]
        self.groups = [group]

    def info(self):
        return f"<Teacher: {self.name}, subjects: {self.subjects}, groups: {self.groups}, salary: {self.salary}>"

    def assign_subject(self, subject_name):
        self.subjects.append(subject_name)

    def assign_group(self, group_name):
        self.groups.append(group_name)

    def get_all_subjects(self):
        return self.subjects


class Student(Person):
    def __init__(self, name, age, group, year, status):
        super().__init__(name, status)
        self.age = age
        self.group = group
        self.year = year
        self.avg_grade = 0

    def calculate_avg_grade(self, grades):
        self.avg_grade = sum(grades) / len(grades)
        return self.avg_grade

    def info(self):
        return f"<Student: {self.name}, group: {self.group}, avg_grade: {self.avg_grade}>"

s1 = Student('abc', 10, 'a1', 5, '-')
s2 = Student('cde', 11, 'a2', 5, '-')

print(s1.name)
print(s2.name)
print(s1.info())
print(s2.info())

teacher = Teacher('ABC', 123, "math", "a1")
teacher.assign_subject('biology')
print(teacher.info())
print(teacher.name)
print(teacher.get_all_subjects())
