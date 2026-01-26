"""
Напишіть клас TypeDecorators, який має кілька методів
для перетворення результатів функцій до заданого типу (якщо це можливо):
методи:
to_int
to_str
to_bool
до_числа
Не забудьте використовувати @wraps
"""

from functools import wraps

class TypeDecorators:
    @staticmethod
    def convert(to_type):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                try:
                    if to_type is bool and isinstance(result, str):
                        return result.strip().lower() in ("true", "1", "yes", "y")
                    return to_type(result)
                except (ValueError, TypeError):
                    return result
            return wrapper
        return decorator

    to_int = convert.__func__(int)
    to_str = convert.__func__(str)
    to_bool = convert.__func__(bool)
    to_float = convert.__func__(float)
@TypeDecorators.to_int
def do_nothing(string: str):
    return string

@TypeDecorators.to_bool
def do_something(string: str):
    return string

print(do_nothing('25'))
print(do_something('True'))

assert do_nothing('25') == 25
assert do_something('True') is True