from tkinter import*
def kvadrat(event=None):
    a = int(edit1.get())
    edit2.delete(0, END)
    edit2.insert(0, str(a**2))
def delete(event=None):
    edit1.delete(0, END)
    edit2.delete(0, END)
root = Tk()
root.geometry('300x300+600+200')
Label(text = 'a = ').grid(row = 0, column = 0, padx = 20, pady =20)
edit1 = Entry(width = 15)
edit1.grid(row = 0, column = 1, padx = 10, pady = 10)
Label(text = 'a**2 = ').grid(row = 1, column = 0, padx = 10, pady = 10)
edit2 = Entry(width = 15)
edit2.grid(row = 1, column = 1, padx = 8, pady = 8)

button1=Button(text='Обчислити',width = 15)
button1.grid(row = 2, column = 1,padx = 10, pady = 10)
button1.bind('<Return>',kvadrat)

button2=Button(text="Очистити",width = 15)
button2.grid(row = 3, column = 1,padx = 10, pady = 10)
button2.bind('<c>',delete)

root.mainloop()