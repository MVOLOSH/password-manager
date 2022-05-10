from tkinter import *
from tkinter import messagebox


def save_to_file():
    if len(website_enter.get()) == 0 or len(password_enter.get()) == 0:
        messagebox.showinfo(title="Oops", message="Dont leave empty fields!")
    else:
        is_okay = messagebox.askokcancel(title="website", message=f"Email/Username: {email_enter.get()}"
                                                                  f"\nPassword: {password_enter.get()}"
                                                                  f"\nDo you want to save it?")
        if is_okay:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website_enter.get()} \t|\t {email_enter.get()} \t|\t {password_enter.get()}\n")
                website_enter.delete(0, END)
                email_enter.delete(0, END)
                password_enter.delete(0, END)
                website_enter.focus()


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
website_enter.grid(row=1, column=1, columnspan=2)
website_enter.focus()

email_enter = Entry(width=30)
email_enter.grid(row=2, column=1, columnspan=2)

password_enter = Entry(width=30)
password_enter.grid(row=3, column=1, columnspan=2)

generate_password_button = Button(text="Generate Password", width=25)
generate_password_button.grid(row=4, column=1, columnspan=2)

add_button = Button(text="Add", width=25, command=save_to_file)
add_button.grid(row=5, column=1, columnspan=2)

window.mainloop()
save_to_file()
