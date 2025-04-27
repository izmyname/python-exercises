import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def random_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = []

    nr_letters = random.randint(6, 8)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    def add_symbols(rand_num, charlist):
        
        password.extend([random.choice(charlist) for char in range(rand_num)])

    add_symbols(nr_letters, letters)
    add_symbols(nr_numbers, numbers)
    add_symbols(nr_symbols, symbols)

    random.shuffle(password)
    random_password = ''.join(password)
    pyperclip.copy(random_password)
    
    pass_entry.delete(0, "end")
    pass_entry.insert(0, random_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    
    website = website_entry.get()
    email = login_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(title="Empty field", message="There shouldn't be empty fields")
    else:
        is_ok =  messagebox.askokcancel(title="nope", message=f"Website: {website}\nEmail: {email}\nPassword: {password}\n\n Proceed?")
        
        if is_ok:
            try:
                with open("my_pass_database.json", "r") as database:
                    # json.dump(new_data, database, indent=4)
                    data = json.load(database)
            except FileNotFoundError:
                with open("my_pass_database.json", "w") as database:
                    json.dump(new_data, database, indent=4)
            else:  
                with open("my_pass_database.json", "w") as database:
                    data.update(new_data)
                    json.dump(data, database, indent=4)
            finally:
                website_entry.delete(0, 'end')
                pass_entry.delete(0, 'end')

# ---------------------------------- SEARCH ------------------------------------- #
def search():

    website = website_entry.get()

    try:
        with open("my_pass_database.json", "r") as database:
            data = json.load(database)
    except FileNotFoundError:
        return messagebox.showinfo(title="no data", message="The database is empty")
    else:
        if website in data:
            return messagebox.showinfo(title="info", message=f"{website}\n\nEmail: {data[website]["email"]}\nPassword: {data[website]["password"]}")   
        else:
            return messagebox.showinfo(title="website not found", message=f"No saved data for {website}")
# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx = 30, pady=30)

canvas = tk.Canvas(width=200, height=200)
logo = tk.PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo)
canvas.grid(column=1, row=0)

website_label = tk.Label(text="Website: ")
website_label.grid(column=0, row=1)

website_entry = tk.Entry(width=21)
website_entry.grid(column=1, row=1,sticky='we')
website_entry.focus()

login_label = tk.Label(text="Email/Username: ")
login_label.grid(column=0, row=2)

login_entry = tk.Entry(width=35)
login_entry.grid(column=1, row=2, columnspan=2, sticky='we')
login_entry.insert(0,"not_a_giant_spider@tarantula.me")

pass_label = tk.Label(text="Password: ")
pass_label.grid(column=0, row=3)

pass_entry = tk.Entry(width=21)
pass_entry.grid(column=1, row=3, sticky='we')

gen_pass_button = tk.Button(text="Generate Password", command=random_password)
gen_pass_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky='we')

search_button = tk.Button(text="Search", width=14, command=search)
search_button.grid(column=2, row=1, sticky='we')

window.mainloop()