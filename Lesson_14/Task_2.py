"""Напишіть декоратор, який приймає список стоп-слів
 та замінює їх на * всередині декорованої функції.
 def stop_words(words: list):

    pass

@stop_words(['pepsi', 'BMW'])

def create_slogan(name: str) -> str:

return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

 """

def stop_words(words):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            # Замінюємо всі стоп-слова
            for w in words:
                result = result.replace(w, '*')
            return result
        return wrapper
    return decorator

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"
print(create_slogan("Steve"))
