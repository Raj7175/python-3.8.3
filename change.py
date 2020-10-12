#On Button click change label value base on entry widget's set value.
from tkinter import *

t=Tk()
t.geometry("250x250")
t.title("Cobination on three widget")
def change():
    l.config(text=e.get())
b=Button(t,text="Click ",command=change)
b.pack()
e=Entry(t)
e.pack()
l=Label(t,text="Hello Visiter Enter your text in Entry lable")
l.pack()
t.mainloop()
