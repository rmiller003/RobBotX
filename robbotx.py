# This is a simple chatbot app programmed in Python 3.9 using tkinter for a GUI interface
# Written by Robert Miller

from tkinter import *
import random, datetime, calendar

root=Tk()
def send():
    send=e.get()
    txt.insert(END,"\n"+send)
    if(e.get()=="Hello"):
        txt.insert(END,"\n"+"RobBot => Hi")
    elif(e.get()=="Hi"):
        txt.insert(END,"\n"+"RobBot => Hello")
    elif(e.get()=="how are you"):
        txt.insert(END,"\n"+"RobBot => I'm fine and you?")
    elif(e.get()=="fine"):
        txt.insert(END,"\n"+"RobBot => Nice to hear")
    elif(e.get()=="what's your name"):
        txt.insert(END,"\n"+"RobBot => I'm the RobBot, it's nice to meet you")
    elif(e.get()=="I have a question"):
        txt.insert(END,"\n"+"Ok, how can I help?")
    elif(e.get()=="where do you live"):
        txt.insert(END,"\n"+"9 Dunnville Rd, Robert's computer Lab, Keswick")
    elif(e.get()=="are u a robot"):
        txt.insert(END,"\n"+"I am an Artificial Intelligence designed to answer your questions ")
    elif(e.get()=="what time is it"):
        txt.insert(END,"\n"+"Please use the following link for local Eastern Standard Time > https://www.timeanddate.com/worldclock/canada/toronto")




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

