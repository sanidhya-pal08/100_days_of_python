import time
from functools import wraps
def cache(func):
    cache_memory={}
    def modified_fx(*args):
        if args in cache_memory:
            return cache_memory[args]
        result=func(*args)
        cache_memory[args]=result
        return result
    return modified_fx

@cache
def long_running_function(a,b):
    time.sleep(4)
    return a+b

print(long_running_function(2,3))
print(long_running_function(2,3))
print(long_running_function(4,3))
print(long_running_function(2,3))