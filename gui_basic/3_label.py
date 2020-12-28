from tkinter import *

root = Tk()
root.title ("Nado GUI")
root.geometry("640x480")

label1 = Label(root, text="안녕하세요")

label1.pack()

photo = PhotoImage (file="D:\Program Files\PythonTutorial\mysite\gui_basic\img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="Meet Again")

    global photo2
    photo2 = PhotoImage (file="D:\Program Files\PythonTutorial\mysite\gui_basic\img2.png")
    label2.config(image=photo2)


btn = Button(root, text="Click", command=change)
btn.pack()

root.mainloop()