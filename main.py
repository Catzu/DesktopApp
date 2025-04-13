from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('App name')
window.geometry('400x400')

def message():
    messagebox.showinfo("popup window tekst", "popup window message")

text = Label(window, text='Title tekst')
text.pack()

btn = Button(window, text="Test button", command=message)
btn.pack()

window.mainloop()