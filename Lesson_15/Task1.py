class Person():
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
my_person = Person('Anna', 'Rudak', '31')
print(f"Привіт, мене звати", my_person.firstname, my_person.lastname, "і мені", my_person.age, "рік.")