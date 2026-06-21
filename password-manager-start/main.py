from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pw():
    letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = list("0123456789")
    symbols = list("!#$%&()*+")

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = (
        [random.choice(letters) for _ in range(nr_letters)] +
        [random.choice(symbols) for _ in range(nr_symbols)] +
        [random.choice(numbers) for _ in range(nr_numbers)]
    )

    random.shuffle(password_list)
    password = "".join(password_list)

    pw_entry.delete(0, END)
    pw_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    pw = pw_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": pw,
        }
    }

    if len(website) == 0 or len(pw) == 0:
        messagebox.showinfo(title="Oops!", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = {}

        data.update(new_data)

        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=5)

        website_entry.delete(0, END)
        pw_entry.delete(0, END)
        
def find_password():
    website=website_entry.get()
    try:
        with open("data.json") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data File Found.")  
    else:    
        if website in data:
            email=data[website]["email"]
            pw=data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {pw}")
        else:
            messagebox.showinfo(title="Error",message=f"No details for {website} exists.")

    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=200, height=200, highlightthickness=0, bg="white")
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0)

website_entry = Entry(width=39)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=39)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "vighneshvelpula10@gmail.com")

pw_entry = Entry(width=21)
pw_entry.grid(row=3, column=1)

pw_button = Button(text="Generate Password", command=gen_pw)
pw_button.grid(row=3, column=2)

search_button = Button(text="Search",bg="blue",command=find_password,width=13)
search_button.grid(row=1, column=3)

add_button = Button(text="Add", width=34, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()