# This is a simple chatbot app programmed in Python 3.9 using tkinter for a GUI interface
# Written by Robert Miller

from tkinter import *
root=Tk()
def send():
    send=e.get()
    txt.insert(END,"\n"+send)
    if(e.get()=="Hello"):
        txt.insert(END,"\n"+"RobBot => Hi")
    elif(e.get()=="hi"):
        txt.insert(END,"\n"+"RobBot => Hello")
    elif(e.get()=="how are you"):
        txt.insert(END,"\n"+"RobBot => I'm fine and you?")
    elif(e.get()=="fine"):
        txt.insert(END,"\n"+"RobBot => Nice to hear")
    else:
        txt.insert(END,"\n"+"RobBot => Sorry I didn't understand that!?!?")
    e.delete(0,END)
txt=Text(root)
txt.grid(row=0,column=0,columnspan=2)
e=Entry(root,width=100)
send=Button(root,text="Send",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title("RobBotX")
root.mainloop()

