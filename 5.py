from tkinter import *

root = Tk()
root.geometry('300x300+500+200')
val = StringVar()
val.set("blue")

colors = ["blue", "yellow", "green", "red"]

def color(event=None):
    label.config(bg=val.get())


i = 0
for color_name in colors:
    rb = Radiobutton(root, text=color_name.capitalize(), variable=val, value=color_name)
    rb.place(x=50, y=50 + i * 30)
    root.bind('<Return>',color)
    i += 1  

label = Label(root, text="Фон мітки")
label.place(x=120, y=180)

root.mainloop()
