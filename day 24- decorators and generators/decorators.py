
# def greet(fx):
#     def mfx():
#         print("hello this is start of the decorator")
#         fx()
#         print("hello this is end of the decorator")
#     return mfx



# def hello():
#     print("hello")
# greet(hello)()
def greet(fx):
    def mfx(*args,**kwargs):
        print("hello")
        fx(*args,**kwargs)
        print("bye")
    return mfx
@greet
def add(a,b):
    print(a+b)

add(7,4)