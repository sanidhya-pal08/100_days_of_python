nums=[4,5,3,4,6,7,7]
# result={x:x**x for x in nums} dictionary comprehension
#result={x*2 for x in nums} set comprehension
result=[x**3 for x in nums if x<5] #list comprehension
print(result)
genretor_obj=(x*2 for x in nums)
print(next(genretor_obj))
next(genretor_obj)
print(next(genretor_obj))