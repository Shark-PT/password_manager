from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website= website_entry.get()
    email = email_entry.get()
    password = password_input.get()
    with open("data.txt", "a") as data:
        data.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, END)
        email_entry.delete(0, END)
        password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(0, "jccreis@gmail.com")

password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky="EW")

password_button = Button(text="Generate Password")
password_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")








window.mainloop()
