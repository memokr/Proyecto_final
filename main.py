#imports
from tkinter import *
import os
from PIL import ImageTk, Image

#Pantalla principal

master = Tk()
master.title('Proyecto final')

img = Image.open('secure.png')
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

Label(master, text = "Sofware Banco", font=('Calibri', 14)).grid(row=0, sticky=N,pady=10)
Label(master, text = "El banco más seguro de todo Metrociudad", font=('Calibri', 12)).grid(row=1, sticky=N)
Label(master, image=img).grid(row=2,sticky=N,pady=15)

def register():
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()

    register_screen = Toplevel(master)
    register_screen.title('Register')
    Label(register_screen, text="Porfavor ingresa tu información para el registro ", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(register_screen, text="Nombre ", font=('Calibri', 12)).grid(row=1, sticky=W)
    Label(register_screen, text="Edad", font=('Calibri', 12)).grid(row=2, sticky=W)
    Label(register_screen, text="Sexo", font=('Calibri', 12)).grid(row=3, sticky=W)
    Label(register_screen, text="Contraseña", font=('Calibri', 12)).grid(row=4, sticky=W)

    Entry(register_screen, textvariable=temp_name).grid(row=1,column=0)
    Entry(register_screen, textvariable=temp_age).grid(row=2, column=0)
    Entry(register_screen, textvariable=temp_gender).grid(row=3, column=0)
    Entry(register_screen, textvariable=temp_password).grid(row=4, column=0)


def login():
    print("esta es la pagina de login")

Button(master, text="Registro", font=('Calibri',12),width=20, command=register).grid(row=3,sticky=N)
Button(master, text="Log in", font=('Calibri',12),width=20,command=login).grid(row=4,sticky=N,pady=10)

master.mainloop()