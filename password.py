import random
from tkinter import *
root = Tk()
root.title('PASSWORD GENERATOR')
root.geometry("450x500")
root.configure(bg='lightblue')


letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV'
special_symbols = '0123456789#_!*&$%?>.'
characters = letters + special_symbols
Label_characters = Label(root, text='', font=('Arial', 12)).pack(padx=10)

character_length = Entry(root, font='Arial 14')
character_length.pack(padx=10)

label = Label(root, text= 'ENTER LENGTH') 
label.place(x=20, y=30)

def generate_password():
    length = character_length.get()
    password = "".join(random.sample(characters, int(length)))
    Label_password.config(text='YOUR NEW PASSWORD:' + password)

Button(root, text='PASSWORD', command=generate_password, font=('Arial', 12)).pack(padx=10)
Label_password = Label(root, font=('Arial', 12))
Label_password.pack()



root.mainloop()
