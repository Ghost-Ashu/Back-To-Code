from re import A
import tkinter as tk
from turtle import bgcolor, color
mayur=tk.Tk()
mayur.title("CALCULATOR")
#--------variables-----------#
global g
g=0
#funcution for the numbers button
def passv(num):
    s=str(ec.get())+str(num)
    ec.delete(0,tk.END)   #have to search how its work means how delete use in entry box and what is tk.end
    ec.insert(0,s)
def clears():
    ec.delete(0,tk.END)
def add():
    a=g
    g=a+int(ec.get())
    ec.delete(0,tk.END)
def equaltoo():
    g=g+int(ec.get())
    ec.delete(0,tk.END)
    ec.insert(0,a)
    a=0
    

##------------gui start here----------------------#
ec=tk.Entry(mayur,width=45,borderwidth=5)
ec.grid(row=0,column=0,columnspan=4,padx=10,pady=0)
#1st row of the button inn claculator
btn1=tk.Button(mayur,text='7',padx=15,pady=15,command=lambda:passv(7)).grid(row=1,column=0,padx=25,pady=10)
btn1=tk.Button(mayur,text='8',padx=15,pady=15,command=lambda:passv(8)).grid(row=1,column=1,padx=25,pady=10)
btn1=tk.Button(mayur,text='9',padx=15,pady=15,command=lambda:passv(9)).grid(row=1,column=2,padx=25,pady=10)
#2st row of the button inn claculator
btn2=tk.Button(mayur,text='4',padx=15,pady=15,command=lambda:passv(4)).grid(row=2,column=0,padx=25,pady=10)
btn2=tk.Button(mayur,text='5',padx=15,pady=15,command=lambda:passv(5)).grid(row=2,column=1,padx=25,pady=10)
btn2=tk.Button(mayur,text='6',padx=15,pady=15,command=lambda:passv(6)).grid(row=2,column=2,padx=25,pady=10)
#3st row of the button inn claculator
btn3=tk.Button(mayur,text='1',padx=15,pady=15,command=lambda:passv(1)).grid(row=3,column=0,padx=25,pady=10)
btn3=tk.Button(mayur,text='2',padx=15,pady=15,command=lambda:passv(2)).grid(row=3,column=1,padx=25,pady=10)
btn3=tk.Button(mayur,text='3',padx=15,pady=15,command=lambda:passv(3)).grid(row=3,column=2,padx=25,pady=10)
#4th row for equal too and zero button
btn4=tk.Button(mayur,text='0',padx=15,pady=15,command=lambda:passv(3)).grid(row=4,column=0,padx=5,pady=5)
btn4=tk.Button(mayur,text='=',width=15,padx=15,pady=15,command=equaltoo).grid(row=4,column=1,columnspan=2,padx=10,pady=10)
#5th row for add and subtract button 
btn5=btn3=tk.Button(mayur,text='add',width=15,padx=15,pady=15,command=add).grid(row=5,column=0,columnspan=2)
btn5=btn3=tk.Button(mayur,text='sub',width=10,padx=15,pady=15,command=lambda:passv(3)).grid(row=5,column=2,)
#row 6th clean button
btn5=btn3=tk.Button(mayur,text='clear',width=32,padx=15,pady=15,command=clears).grid(row=6,column=0,columnspan=3,padx=10,pady=10)




#mayur.resizable(False,False)
mayur.mainloop()
