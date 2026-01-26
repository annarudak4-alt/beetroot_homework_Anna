"""
Task 3
Fraction
Створіть клас Fraction, який буде представляти всю базову
арифметичну логіку для дробів (+, -, /, *) з належною перевіркою
й обробкою помилок. Потрібно додати магічні методи для математичних
операцій та операції порівняння між об'єктами класу Fraction
"""
"""class Fraction:
    pass

if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    x + y == Fraction(3, 4)
    """
class Fraction:
    def __init__(self, numerator, denominator):
        self.n = numerator
        self.d = denominator

    def __repr__(self):
        # Повертає зручне текстове представлення об’єкта
        return f"Fraction({self.n}, {self.d})"

    # Додавання дробів
    def __add__(self, other):
        num = self.n * other.d + other.n * self.d
        den = self.d * other.d
        return Fraction(num, den)

    # Віднімання дробів
    def __sub__(self, other):
        num = self.n * other.d - other.n * self.d
        den = self.d * other.d
        return Fraction(num, den)

    # Множення дробів
    def __mul__(self, other):
        return Fraction(self.n * other.n, self.d * other.d)

    # Ділення дробів
    def __truediv__(self, other):
        if other.n == 0:
            raise ZeroDivisionError("Ділення на нуль неможливе.")
        return Fraction(self.n * other.d, self.d * other.n)

    # Порівняння дробів
    def __eq__(self, other):
        # Порівнюємо через добутки
        return self.n * other.d == other.n * self.d


if __name__ == "__main__":
    x = Fraction(1, 2)     # створюємо дріб 1/2
    y = Fraction(1, 4)     # створюємо дріб 1/4
    print(x + y == Fraction(3, 4))
