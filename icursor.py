#Set cursor position as your choice position
from tkinter import *
from tkinter import font#it import to font in code
t=Tk()
t.geometry("300x300")
f=font.Font(size=25,family="MT BOLD")#set one style in variable 'f'
t.title("Operation on string which set by entry control")
s=StringVar()#dynamic variable for change value 
def change():#it implement on button click
    e.icursor(2) 
    

b=Button(t,text="one Click set cursor position ",command=change)
b.pack()
e=Entry(t,textvariable=s)
e.pack()

t.mainloop()
