from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=250, width=250)
logo = PhotoImage(file="logo.png")
canvas.create_image(125, 125, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)


website_enter = Entry(width=30)
website_enter.grid(row=1,column=1,columnspan=2)

email_enter = Entry(width=30)
email_enter.grid(row=2,column=1,columnspan=2)

password_enter = Entry(width=30)
password_enter.grid(row=3,column=1,columnspan=2)

generate_password_button = Button(text="Generate Password",width=25)
generate_password_button.grid(row=4,column=1,columnspan=2)

add_button = Button(text="Add",width=25)
add_button.grid(row=5,column=1,columnspan=2)





window.mainloop()
