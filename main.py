import json
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

    new_data = {
        f"{website}": {
            "email": email,
            "password": password_entry,
        }
    }

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

            try:
                with open("data.json", "r") as data_file:
                    current_data = json.load(data_file)
                    current_data.update(new_data)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                with open("data.json", "w") as data_file:
                    json.dump(current_data, data_file, indent=4)

            messagebox.showinfo(message="Details saved successfully")

            website_input.delete(0, END)
            password_input.delete(0, END)
# ---------------------------- Search Website ------------------------------- #


def search():
    website = website_input.get()

    try:
        with open("data.json") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title=f"No details saved", message="You have no website login details saved.\n"
                                                               "Please save details for a site before searching.")

    else:
        try:
            messagebox.showinfo(title=f"{website}", message=f""
                                                            f"Email: {data[website]['email']}\n"
                                                            f"Password: {data[website]['password']}")
        except KeyError or FileNotFoundError:
            messagebox.showinfo(title=f"{website} not Found", message=f"Login details for {website} not found."
                                                                      f"Please add details for {website}.")

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
