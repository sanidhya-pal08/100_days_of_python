import time
from functools import wraps
def cache(func):
    cache_value={}
    print(cache_value)
    @wraps(func)
    def wrapper(*args,**kwargs):
        if args in cache_value:
            return cache_value[args]
        result=func(*args,**kwargs)
        cache_value[args]=result
        return result
    return wrapper

@cache
def long_running_function(a,b):
    time.sleep(4)
    return a+b

print(long_running_function(2,3))
print(long_running_function(2,3))
print(long_running_function(4,3))
print(long_running_function(2,3))