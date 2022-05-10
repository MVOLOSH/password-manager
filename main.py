from tkinter import *

window = Tk()
window.title("password manager")
window.config(padx=25,pady=25)

canvas = Canvas(height=250, width=250)
logo = PhotoImage(file="logo.png")
canvas.create_image(125,125,image=logo)
canvas.pack()

window.mainloop()