"""
Магазин товарів

Напишіть клас Product, який має три атрибути:
type
name
price
Потім створіть клас ProductStore, який матиме деякі Products та працюватиме з усіма товарами
в магазині. Усі методи, у випадку, якщо вони не можуть виконати свою дію, повинні викликати
ValueError з відповідною інформацією про помилку.
Поради: Використовуйте концепції агрегації/композиції під час реалізації класу ProductStore.
Ви також можете реалізувати додаткові класи для роботи з певним типом продукту тощо.
Також клас ProductStore повинен мати такі методи:
add(product, amount) - одає задану кількість одного товару із заздалегідь визначеною премією
до ціни для вашого магазину (30 відсотків)
set_discount(identifier, percent, identifier_type='name') – додає знижку для всіх товарів,
зазначених у вхідних ідентифікаторах (тип або назва). Знижка має бути вказана у відсотках
sell_product(назва_продукту, кількість) – видаляє певну кількість товарів з магазину, якщо
вони доступні, в іншому випадку викликає помилку. Також збільшує дохід, якщо метод sell_product
виконується успішно.
get_income() - повертає суму, зароблену екземпляром ProductStore.
get_all_products() – повертає інформацію про всі доступні товари в магазині.
get_product_info(product_name) – повертає кортеж з назвою продукту та кількістю товарів у магазині.
"""

class Product:
    def __init__(self, type, name, price):
        self.type = type  # тип товару ('Food')
        self.name = name  # назва товару ('Ramen')
        self.price = price  # ціна товару

class ProductStore:
    def __init__(self):
        self.products = {}  # тут зберігаються товари магазину
        self.income = 0  # дохід магазину

    def add(self, product, amount):
        # додавання товар у магазин з націнкою 30%
        price_with_premium = product.price * 1.3
        if product.name in self.products:
            self.products[product.name]['amount'] += amount
        else:
            self.products[product.name] = {
                'product': product,
                'amount': amount,
                'price': price_with_premium,
                'discount': 0
            }
    def set_discount(self, identifier, percent, identifier_type='name'):
        # встановлюємо знижку (за назвою або типом)
        for item in self.products.values():
            if (identifier_type == 'name' and item['product'].name == identifier) or \
                    (identifier_type == 'type' and item['product'].type == identifier):
                item['discount'] = percent

    def sell_product(self, product_name, amount):
        # продаж товару
        if product_name not in self.products:
            raise ValueError("Такого товару немає")
        if self.products[product_name]['amount'] < amount:
            raise ValueError("Недостатньо товару")

        item = self.products[product_name]
        # враховуємо знижку
        price_after_discount = item['price'] * (1 - item['discount'] / 100)
        self.income += price_after_discount * amount
        item['amount'] -= amount

    def get_income(self):
        return self.income

    def get_all_products(self):
        return [(p['product'].name, p['amount']) for p in self.products.values()]

    def get_product_info(self, product_name):
        item = self.products[product_name]
        return (item['product'].name, item['amount'])

p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()
s.add(p, 10)
s.add(p2, 300)

s.sell_product('Ramen', 10)

print(s.get_product_info('Ramen'))  # ('Ramen', 290)
