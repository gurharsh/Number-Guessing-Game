import random
from tkinter import *
root=Tk()
root.title("Number Guessing Game")
root.geometry("600x400")
root.wm_iconbitmap("game.ico")
root.config(background="#FFFFFF")
attempts=10
answer=random.randint(1,99)
# print(answer) # for the random number
def check_ans():
    global attempts
    global text
    attempts-=1
    guess=ent.get()
    if(answer==guess):
        text.set("Congrats ! You are Winner")
        btn_chk.place_forget()
    elif(attempts==0):
        text.set("You are out of attempts")
        btn_chk.place_forget()
    # elif(guess<answer):
    #     text.set("Incorrect You have remaining "+str(attempts)+" to guess the number. Enter higher number")
    # elif(guess>answer):
    #     text.set("Incorrect You have remaining "+str(attempts)+" to guess the number. Enter lower number")
    elif(guess<answer or guess>answer):
        text.set("Incorrect You have \nremaining "+str(attempts))

ent=IntVar()
lb1=Label(root,text="Enter Number between\n 1-99",bg="#FFFFFF",font=("Times New Roman",13,"bold"))
lb1.place(x=390,y=90)
Entry(root,textvariable=ent,bg="#FFFFFF",fg="#466E8D",font=("arial",'15',"bold")).place(x=370,y=150)
btn_chk=Button(root,text="Check",bg="#466E8D",font=("Times New Roman",12,"bold"),command=check_ans)
Button(root,text="Quit",bg="#466E8D", font=("Times New Roman",12,"bold"),command=root.destroy).place(x=500,y=250)
btn_chk.place(x=410,y=250)
text=StringVar()
text.set("You have 10 attempts\n to guess the number")
Label(root,textvariable=text,bg="#FFFFFF",font=("Times New Roman",15),fg="#E7CF50").place(x=370,y=190)
bgimg = PhotoImage(file="guess.png")
lbl_img = Label(root, image=bgimg, bg="#FFFFFF")
lbl_img.place(x=0,y=0)
root.mainloop()