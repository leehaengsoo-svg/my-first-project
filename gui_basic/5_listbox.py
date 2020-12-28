from tkinter import *

root = Tk()
root.title ("Nado GUI")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=3)
listbox.insert(0,"Apple")
listbox.insert(1,"Strawberry")
listbox.insert(2,"Banana")
listbox.insert(END, "Watermelon")
listbox.insert(END, "Graph")
listbox.pack()

def btncmd():
    pass

btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()