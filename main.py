from tkinter import *
from tkinter import messagebox
from passwordgenerator import password
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_input.delete(0, END)
    password_input.insert(0, f"{password()}")
    user_password = password()
    pyperclip.copy(user_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    email = email_input.get()
    password_entry = password_input.get()
    details = False

    if website == '':
        messagebox.showerror(title="Website Name Error", message="Please insert the website name.")
    elif email == '':
        messagebox.showerror(title="Email Error", message="Please insert a valid email address.")
    elif password_entry == '':
        messagebox.showerror(title="Password Error", message="Please insert a password.")
    else:
        details = True

    if details:

        correct = messagebox.askokcancel(title=f"{website}", message=f"Are these details correct? \nWebsite:{website}\n"
                                                                     f"Email:{email}\nPassword:{password_entry}\n")
        if correct:
            messagebox.showinfo(message="Details saved successfully")
            file = open("data.txt", "a")
            file.write(f"{website} | {email} | {password_entry}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)
            file.close()
# ---------------------------- Search Website ------------------------------- #


def search():

    with (open("data.txt") as file):
        lines = file.readlines()
        found = False
        for line in lines:
            words = line.strip()
            site_name = website_input.get()
            if site_name in line:
                words = words.split("|")
                messagebox.showinfo(title="Details",
                                    message=f"Website:{words[0]}\nEmail:{words[1]}\nPassword:{words[2]}")
                found = True
        if not found:
            messagebox.showinfo(title="Website Error", message=f"{site_name} login details are not saved.")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("(Password Manager")
window.config(padx=50, pady=50)


# LOGO #

lock = Canvas(width=200, height=200)
lock.grid(row=0, column=1)
image = PhotoImage(file="logo.png")
lock.create_image(100, 100, image=image)

# COLUMN 1 Elements #

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# COLUMN 2 Elements #

website_input = Entry(width=35)
website_input.grid(row=1, column=1)
website_input.focus()


email_input = Entry(width=53)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "email@email.com")

password_input = Entry(width=35)
password_input.grid(row=3, column=1)


add_button = Button(text="Add", width=45, command=save)
add_button.grid(row=4, column=1, columnspan=2)

# Column 3 Elements #

generate_button = Button(text="Generate Password", width=14, command=generate_password)
generate_button.grid(row=3, column=2)

search_button = Button(text="Search", width=14, command=search)
search_button.grid(row=1, column=2)


window.mainloop()
