import random
import string as st
from tkinter import *
from tkinter import messagebox
import os 

class Random_Generator:

    def __init__(self):
        random.seed(random.randint(0, 100))

    def generator_function(self, keyphrase):
        contains_special=False
        contains_digit=False
        contains_capital=False 
        password = ""
        max_length=16
        every_Char=st.ascii_letters+st.digits+st.punctuation 
        for i in range(len(keyphrase)):
            if(keyphrase[i] in st.ascii_uppercase and not contains_capital):
                contains_capital=True
                password+=keyphrase[i]
                continue 
            if(keyphrase[i] in st.digits and not contains_digit):
                contains_digit=True
                password+=keyphrase[i]
                continue 
            if(keyphrase[i] in st.punctuation and not contains_special):
                password+=keyphrase[i]
                contains_special=True
        if(not contains_special):
            password+=random.choice(st.punctuation)
        if(not contains_capital):
            password+=random.choice(st.ascii_uppercase)
        if(not contains_digit):
            password+=random.choice(st.digits)
        if(len(keyphrase)<1):
            for i in range(max_length-3):
                password+=random.choice(every_Char)
        else:
            for i in range(max_length-len(password)):
                password+=random.choice(keyphrase)
        return password


if os.path.exists("password.txt"):
    pass
else:
    file=open("password.txt","w")
    file.close()
file=open("password.txt",'a')
generate=Random_Generator()
window = Tk()
window.title("PasswordGenerator")
window.geometry('300x100')
label=Label(window,text="Enter keyphrase for your password")
label.grid(column=0,row=0)
inp=Entry(window,width=10)
inp.grid(column=1,row=0)
def clicked():
    password=generate.generator_function(inp.get())
    file.write(password)
    file.close()
    messagebox.showinfo('Password Generated','The password generated is '+password)
enter_button=Button(window,text="Enter",command=clicked)
enter_button.grid(column=2,row=0)
window.mainloop()

        
