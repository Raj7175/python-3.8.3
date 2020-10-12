#image place on background
from tkinter import *

t = Tk()


bimg = PhotoImage(file = "C:\\Users\\Divyaraj\\Desktop\\p.png")#object of image it support only png formate.
background_label = Label(t, image=bimg)#bind image by its variable
background_label.place(x=0, y=0, relwidth=1, relheight=1)#set position


t.mainloop
