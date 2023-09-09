from tkinter import *

import os

mk=Tk()

mk.title('Age and Gender Detection System')

mk.geometry('1200x600')

mk.config(bg="lime")

l1=Label(mk,width="35",height="4",text="Age and Gender Detection 

System",fg="red",bg="black",font="timesroman 20")

l1.pack(pady=20)

bg1=PhotoImage(file="C:/Users/91936/AppData/Local/Programs/Python/Python3

10/mini project/img1.png")

l2=Label(mk,width="265",height="200",image=bg1)

l2.pack(pady=10)

def run_program():

 os.system('python module1.py')

bt1=Button(mk,width="25",height="3",text="module1",fg="purple",bg="blue",co

mmand=run_program,font="verdana 20")

bt1.pack(pady=20)

def run_program2():

 os.system('python module2.py')

bt3=Button(mk,width="25",height="3",text="module2",fg="purple",bg="blue",co

mmand=run_program2,font="verdana 20")

bt3.pack(pady=20)

def close():

 mk.destroy()

bt4=Button(mk,width="25",height="3",text="exit",fg="purple",bg="blue",comman

d=close,font="verdana 20")

bt4.pack(pady=10)

mk.mainloop()
