''' CODSOFT Internship - PYTHON PROGRAMMING 
    TASK 2- TO-DO LIST
    DONE BY DEEPAK RAJ R
'''

import tkinter #creating layout

from tkinter import*

#here we can able to set the frame title,dimensions,pixels,fixing the frame and its background
root =Tk()
root.title("simple calculator by Deepak Raj R")#Tk is define by tkinter and title is given
root.geometry("590x600+200+200")#set the length and width of calculator
root.resizable(False,False)#to lock the length and width
root.configure(bg="#C0C0C0")#color of background

top_icon = PhotoImage(file="Image/cal_icon.png")# to access the file image 
root.iconphoto(False,top_icon)

operation = ""

#operations for enter,clear,calculate the specific operations
def display(value):
   global operation 
   operation+=value
   disvalue.config(text=operation)

#used to clear the operands or restart the calculator
def clear():
    global operation 
    operation=""
    disvalue.config(text=operation)

#used to perform arthmetic operations
def calculate():
    global operation
    result=""
    if operation != "":
        try:
            result=eval(operation)
        except:
            result="Math error"
            operator=""
    disvalue.config(text=result)

#for display unit
disvalue = Label(root,width=25,height=2,text="",font=("arial",30))#here we describe length,width,font of actual display screen
disvalue.pack()


#design the input button in row1 and column0,1,2,3
Button(root,text="/",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#808080",command=lambda : display("/")).place(x=149,y=100)
Button(root,text="c",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#000000",command=lambda : clear()).place(x=10,y=100)
Button(root,text="%",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda : display("%")).place(x=291,y=100)
Button(root,text="*",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda : display("*")).place(x=433,y=100)

#design the input button in row2 and column0,1,2,3
Button(root,text="8",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda : display("8")).place(x=149,y=200)
Button(root,text="7",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda : display("7")).place(x=10,y=200)
Button(root,text="9",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda : display("9")).place(x=291,y=200)
Button(root,text="-",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda : display("-")).place(x=433,y=200)

#design the input button in row3 and column0,1,2,3
Button(root,text="5",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda : display("5")).place(x=149,y=300)
Button(root,text="4",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda : display("4")).place(x=10,y=300)
Button(root,text="6",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda : display("6")).place(x=291,y=300)
Button(root,text="+",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda : display("+")).place(x=433,y=300)

#design the input button in row3 and column0,1,2
Button(root,text="2",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda : display("2")).place(x=149,y=400)
Button(root,text="1",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda : display("1")).place(x=10,y=400)
Button(root,text="3",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda : display("3")).place(x=291,y=400)

#design the input button in row4 and column0,1
Button(root,text="0",width=11,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda : display("0")).place(x=10,y=500)
Button(root,text=".",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda : display(".")).place(x=291,y=500)

#for getting the final result
Button(root,text="=",width=5,height=3,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#000000",command=lambda : calculate()).place(x=433,y=400)

#for the excution of program in loop condition
root.mainloop()


