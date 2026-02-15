double= lambda x:x+x
avg=lambda x,y: (x+y)/2
def appl(fx,value):
    return 6+ fx(value)
print(appl(lambda x:x*x,7))

