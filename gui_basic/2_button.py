from tkinter import *

root = Tk()
root.title ("Nado GUI")
btn1 = Button(root, text="버튼1")
btn1.pack()


btn2 = Button(root, padx=5, pady=10, text="버튼22222222222222222222")
btn2.pack()


btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()


btn4 = Button(root, width=20, height=2,  text="버튼4444444444444444444444444")
btn4.pack()


btn5 = Button(root, fg="red", bg="yellow", width=20, height=2,  text="버튼4444444444444444444444444")
btn5.pack()

photo = PhotoImage(file="D:\Program Files\PythonTutorial\mysite\gui_basic\img.png")
btn6 = Button(root, image=photo)
btn6.pack()
     

def btncmd():
    print("버튼을 클릭 했어요")

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()


root.mainloop()