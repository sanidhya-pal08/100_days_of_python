from functools import reduce 
# #map_function
listt=[1,2,3,4,5]
# newlist=list(map(lambda x: x**3,listt))
# # print(newlist)

# #filter_function
# def filter_function(a):
#     return a>4
# newl=list(filter(filter_function,newlist))
# print(newl)
#reduce function
sum=reduce(lambda x,y:x+y,listt)
print(sum)