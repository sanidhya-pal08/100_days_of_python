def logger(level):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"[{level}] Starting '{func.__name__}'")
            result = func(*args, **kwargs)
            print(f"[{level}] Ending '{func.__name__}'")
            return result
        return wrapper
    return actual_decorator


@logger("DEBUG")
def add(a, b):
    return a + b


@logger("INFO")
def greet(name):
    return f"Hello, {name}"


print(add(10, 5))
print(greet("Sanidhya"))
