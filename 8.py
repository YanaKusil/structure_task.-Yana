from tkinter import *

def Dobutok(event=None):
    N = int(edit1.get())
    d = 1
    for i in range(1 , N + 1):
        d += i
    label2['text'] = "Добуток чисел  1 * 2 * 3 * ... * " + str(N) + " = " + str(d)
    
root = Tk()
root.geometry("450x150")
root.title("Добуток чисел") 
# створити напис та поле введення
label1  = Label(root , text = "Введіть число: ")
label1.place( x = 20 , y = 20)
edit1 = Entry(root)
edit1.place( x = 200 , y = 20 , width = 240)

# створити напис, записати результат
label2 = Label(root , text ="")
label2.place(x = 200 , y = 50 )

# створити кнопку
button1 = Button(root, text = " Обчислити")
button1.place(x = 200 , y = 90 , width = 240)

button1.bind("<Button-1>",Dobutok)
root.mainloop()
