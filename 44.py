def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Фунция шақыру {func.__name__} аргументімен: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Функция {func.__name__} қайтарылды: {result}")
        return result
    return wrapper
@logger
def add(a, b):
    return a + b
result_add = add(3, 5)
