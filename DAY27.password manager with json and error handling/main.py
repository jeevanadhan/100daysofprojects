from tkinter import *
from tkinter import messagebox
from random import randint,shuffle,choice
import pyperclip,json
# ---------------------------- PASSWORD GENERATOR ------------------------------ #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def generate_password():
    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)
    password_list = []
    password_list += [choice(letters) for i in range(randint(8, 10))]
    password_list += [choice(symbols) for j in range(randint(2, 4))]
    password_list += [choice(numbers) for k in range(randint(2, 4))]
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0,END)
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()  # Get value from the first entry
    email = email_entry.get()  # Get value from the second entry
    password = password_entry.get()
    new_data = {
        website: {"email": email,
                  "password": password}
    }
    if not website or not email or not password:
        is_empty = messagebox.showinfo(title="OOPS", message="please dont leave empty fields:")
    else:
        is_ok = messagebox.askokcancel(title="checking",
                                       message=f" Website: {website},\n\n Email/Username: {email},\n\n Password: {password} \n\n is it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except json.JSONDecodeError:
                data={}

            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()

# ---------------------------- SEARCH DATA ------------------------------ #
def find_password():
    website = website_entry.get().title()  # Get value from the first entry
    email = email_entry.get().title()  # Get value from the second entry
    password = password_entry.get().title()
    try:
        with open("data.json","r") as file:
            data=json.load(file)
    except json.JSONDecodeError:
            messagebox.showwarning(message="file not found")
    else:
        data_found=[[value["email"],value["password"]] for key,value in data.items() if key.title()==website and value["email"].title()==email]
        if data_found:
            messagebox.showinfo(title="FOUND",message=f" Email: {data_found[0][0]}\n Password: {data_found[0][1]}")
            pass
        else:
            messagebox.showwarning(title="FILE CHECKING",message="file not found")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PASSWORD MANAGER")
window.config(padx=20, pady=20, bg="black")

canvas = Canvas(width=200, height=200, highlightthickness=0, bg="black")
photoimage = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photoimage)
canvas.grid(row=0, column=1)

website_text = Label(text="Website:", bg="black", fg="white")
website_text.grid(column=0, row=1, sticky="ew", padx=5, pady=5)
website_text.focus()
email_text = Label(text="Email/Username:", bg="black", fg="white")
email_text.grid(column=0, row=2, sticky="ew", padx=5, pady=5)

password_text = Label(text="Password:", bg="black", fg="white")
password_text.grid(column=0, row=3, sticky="ew", padx=5, pady=5)


# entries

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1, columnspan=1, sticky="ew", padx=5, pady=5)
website_entry.focus()
email_entry = Entry(width=47)
email_entry.grid(column=1, row=2, columnspan=2, sticky="ew", padx=5, pady=5)
email_entry.insert(0,"jeeva1234@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, columnspan=1, sticky="ew", padx=5, pady=5)
# BUTTONS
generate_pass_button = Button(text="Generate password",command=generate_password)
generate_pass_button.grid(column=2, row=3, sticky="ew", padx=5, pady=5)

add_button = Button(text="Add", width=40,command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew", padx=5, pady=5)

search_button=Button(text="search",command=find_password)
search_button.grid(column=2, row=1, columnspan=2, sticky="ew", padx=5, pady=5)

window.mainloop()
