from tkinter import *

def Factorial(event=None):
    N = int(edit1.get())
    f = 1
    for i in range(1 , N + 1):
        f = f*i
    # виведення результату в label2
    label2['text'] = "Факторіал числа " + str(N) + "! = " + str(f)
    
    
root = Tk()
root.geometry("420x150")
root.title("Факторіал") 
#  напис та поле введення
label1  = Label(root , text = "Введіть число N  : ")
label1.place( x = 20 , y = 20)
edit1 = Entry(root)
edit1.place( x = 200 , y = 20 , width = 200)

# напис для виведення результату
label2 = Label(root , text ="")
label2.place(x = 200 , y = 50 )

# cстворити кнопку
buton1 = Button(root, text = " Обчислити")
buton1.place(x = 200 , y = 90 , width = 200)

buton1.bind("<Button-1>",Factorial)

root.mainloop()
