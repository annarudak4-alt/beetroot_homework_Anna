"""Математик

Реалізуйте клас Mathematician, який є допоміжним класом для виконання математичних операцій
зі списками.
Клас не приймає жодних атрибутів і має лише методи:
square_nums (приймає список цілих чисел та повертає список квадратів)
remove_positives (бере список цілих чисел і повертає його без додатних чисел)
filter_leaps (бере список дат (цілих чисел) та видаляє ті, що не є «високосними роками»
"""

class Mathematician:
    def square_nums(self, nums):
        return [n ** 2 for n in nums]

    def remove_positives(self, nums):
        return [n for n in nums if n <= 0]

    def filter_leaps(self, years):
        return [y for y in years if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)]

m = Mathematician()

print(m.square_nums([7, 11, 5, 4]))          # [49, 121, 25, 16]
print(m.remove_positives([26, -11, -8, 13, -90]))  # [-11, -8, -90]
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))  # [1884, 2020]