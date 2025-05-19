from tkinter import *
from tkinter import messagebox
import os

def show_photo():
    filename = "lb12.gif"
    if os.path.exists(filename):
        try:
            photo = PhotoImage(file=filename)
            label_photo.config(image=photo)
            label_photo.image = photo  
        except Exception as e:
            messagebox.showerror("Помилка", f"Не вдалося завантажити зображення: {e}")
    else:
        messagebox.showerror("Помилка", f"Файл '{filename}' не знайдено.")

def show_info():
    specialty = entry_specialty.get().strip()
    if specialty == "111М":
        messagebox.showinfo("Про спеціальність",
                            f"{specialty}\nСпеціальність 111 Математика\nОсвітня програма: Комп'ютерна математика")
    elif specialty == "СОМ":
        messagebox.showinfo("Про спеціальність",
                            f"{specialty}\nСпеціальність 014 Середня освіта\nОсвітня програма: Математика, інформатика")
    else:
        messagebox.showinfo("Про спеціальність", f"{specialty}\nТакої спеціальності на факультеті немає")

root = Tk()
root.title("Анкета")
root.geometry("300x500")

Label(root, text="Прізвище:").pack()
entry_surname = Entry(root, width=25)
entry_surname.pack()

Label(root, text="Ім'я:").pack()
entry_name = Entry(root, width=25)
entry_name.pack()

Label(root, text="По батькові:").pack()
entry_patronymic = Entry(root, width=25)
entry_patronymic.pack()

Label(root, text="Стать:").pack()
gender_var = StringVar(value="ч")
Radiobutton(root, text="Чоловіча", variable=gender_var, value="ч").pack()
Radiobutton(root, text="Жіноча", variable=gender_var, value="ж").pack()

Label(root, text="Курс:").pack()
course_var = IntVar(value=1)
for i in range(1, 5):
    Radiobutton(root, text=str(i), variable=course_var, value=i).pack()

Label(root, text="Спеціальність:").pack()
entry_specialty = Entry(root, width=25)
entry_specialty.pack()

Button(root, text="Про спеціальність", width=20, command=show_info).pack(pady=5)
Button(root, text="Показати фото", width=20, command=show_photo).pack(pady=5)

label_photo = Label(root)
label_photo.pack(pady=5)

root.mainloop()