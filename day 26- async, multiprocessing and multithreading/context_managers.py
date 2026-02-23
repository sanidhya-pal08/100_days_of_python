# # file = open("file.txt","r")
# # try:
# #     file.write("hello")
# # finally:
# #     file.close() 


# #completely same as ---------------->

# # with open("file.txt","r") as file:
# #     file.write("hello")

# #writing own context manager

# class File:
#     def __init__(self,filename,method):
#         self.file=open(filename,method)
#     def __enter__(self):  #first thing that happens, it returns a value something that we are gonna use inside a context manager
#         #it gets called first
#         print("enter")
#         return self.file
#     def __exit__(self, type,value,traceback):
#         #exit will always happen even if code crashes to make sure that file closes and data isnt leaked 
#         print(f"{type},{value},{traceback}")
#         print("exit")
#         self.file.close()
#         if type== Exception:
#             return True

# with File("file.txt","w") as f:
#     print("middle")
#     f.write("hellow!!!")
#     raise Exception()##exit is happening even if the exception is happening


         
class File:
    def __init__(self,filename,method):
        self.file=open(filename,method)
    def __enter__(self):
        print("hi")
        return self.file
    def __exit__(self, exc_type, exc, tb):
        print("bye")
        self.file.close()
with File("file.txt","r") as f:
    f.write("hellllll")
