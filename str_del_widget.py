#String delete by specific point and use font style 
from tkinter import *
from tkinter import font#it import to font in code
t=Tk()
t.geometry("300x300")
f=font.Font(size=25,family="MT BOLD")#set one style in variable 'f'
t.title("Operation on string which set by entry control")
s=StringVar()#dynamic variable for change value 
def change():#it implement on button click
    e.delete(1,4) 
    

b=Button(t,text="Click ",command=change)
b.pack()
e=Entry(t,textvariable=s)
e.pack()
l=Label(t,textvariable=s,text="Hello Visiter Enter your text in Entry lable",font=f)#f variable which we define first.
l.pack()
t.mainloop()
