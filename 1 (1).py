from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("300x100+600+400")
str_var=StringVar() # створення об’єкта для отримання значення з текстового поля

def button_click(event=None):     # опрацювання події натиснення кнопки
    messagebox.showinfo("Привітання", "Вітаю " + str_var.get()+"!")

label = Label(text="Введіть ім'я:").pack() # створення текстового напису та його розміщення на головній формі
edit = Entry(root, textvariable=str_var)
edit.pack()
button = Button(root, text="Ok!")
button.pack()
root.bind('<Button-1>',button_click)
root.mainloop() 
