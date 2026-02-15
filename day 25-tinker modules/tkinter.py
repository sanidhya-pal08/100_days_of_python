#tkinter module/package
#widges
#function of tkinters
#frames-container which has collection o widges
#labels-to display text or image
#labelframe-
#button-used to call  function when clicked
#entry box
#text
#message box
#combo box
#list box
#scroll bar
#scale
#canavs
#menu

#wap to display tkinter window
# use  root.mainlooop() to finish the program
from tkinter import Tk
#root=Tk()
#root.mainloop()

#wap to display title window of tkinter
#from tkinter import Tk
#root=Tk();
#root.title("Python is fun proramming lanaguage")
#root.mainloop();

#from tkinter import Tk,Label
#root=Tk();
#msg=Label(root,text="Python is fun programming language")
#msg.pack()
#root.mainloop();
from tkinter import Tk,Label
root=Tk();
root.title("Python is fun proramming language")
msg=Label(root,text="Python is fun programming language")
msg.config(font=('arial',24,'italic bold underline'),fg="yellow")
msg.pack()
root.mainloop();
           
           


