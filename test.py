import tkinter as tk
from tkinter import*
import time
def main():
    root = Tk()
    def close(event):
        root.destroy()
    def info1():
        global lb1
        lb1 = Label(root,text="Sorry,It will take Just one minutes",bd=20,bg="black",fg="white",font=("微软雅黑",65))
        lb1.pack(fill="y",expand=True)
        root.after(6000,info2)
    def info2():
        global lb1
        global lb2
        lb1.pack_forget()
        lb2 = Label(root,text="Today is Saturday, SO...",bd=20,bg="black",fg="white",font=("微软雅黑",80))
        lb2.pack(fill="y",expand=True)
        root.after(5000,info3)

    def info3():
        global lb2
        global lb3
        lb2.pack_forget()
        lb3 = Label(root,text="Happy Weekend, Guys",bd=20,bg="black",fg="white",font=("微软雅黑",80))
        lb3.pack(fill="y",expand=True)
        root.after(6000,info4)

    
    def info4():
            global lb3
            global lb4
            # lb2.pack_forget()
            lb4 = Label(root,text="get the code:https://github.com/Tarkyyyy/",bd=20,bg="black",fg="white",font=("微软雅黑",30))
            lb4.pack(fill="y",expand=True)
            root.after(6000,info5)
    
    def info5():
        lb5 = Label(root,text="I think Penny will forgive me, right?",bd=20,bg="black",fg="white",font=("微软雅黑",30))
        lb5.pack(fill="y",expand=True)
        root.after(3000,info6)

    def info6():
        lb5 = Label(root,text="That's All, Thank you :)",bd=20,bg="black",fg="white",font=("微软雅黑",30))
        lb5.pack(fill="y",expand=True)
        root.after(15000,info7)
        
    def info7():
        lb5 = Label(root,text="如果我现在还没关掉的话那应该是遇到了点问题",bd=20,bg="black",fg="white",font=("微软雅黑",30))
        lb5.pack(fill="y",expand=True)

    root.configure(bg="black")
    root.attributes("-fullscreen", True)
    root.attributes('-topmost', True)
    info1()
    # bt = Button(root,text="123",command=close)
    # bt.pack()
    root.bind("<F11>",close)
    root.mainloop()

if __name__=="__main__":
   main()