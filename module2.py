from tkinter import *

import os

import sys

mk=Tk()

mk.title('Age and Gender Detection System-Module2')

mk.geometry('500x500')

mk.config(bg="seagreen")

l1=Label(mk,width="40",height="4",text="welcome to 

module2",fg="red",bg="black",font="timesroman 30")

l1.pack(pady=20)

def run_program():

 os.system('cmd') 

bt2=Button(mk,width="20",height="4",text="Detect From 

Photos",fg="purple",bg="blue",command=run_program,font="lucida 20")

bt2.pack(pady=20)

def close():

 mk.destroy()

bt4=Button(mk,width="20",height="4",text="exit",fg="purple",bg="blue",command=close,font="

verdana 20")

bt4.pack(pady=20)

mk.mainloop()
