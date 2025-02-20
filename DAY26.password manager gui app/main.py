from tkinter import *
from tkinter import messagebox
from random import randint,shuffle,choice
import pyperclip
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
    data1 = website_entry.get()  # Get value from the first entry
    data2 = email_entry.get()  # Get value from the second entry
    data3 = password_entry.get()
    if not data1 or not data2 or not data3:
        is_empty=messagebox.showinfo(title="OOPS",message="please dont leave empty fields:")
    else:
        is_ok=messagebox.askokcancel(title="checking",message=f"these are the details entered \n website: {data1},\n email/username: {data2},\n password: {data3} \n is it ok to save?")
        if is_ok:
            with open("data.txt","a+") as file:

                file.write(f"{data1} | {data2}| {data3}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)
                website_entry.focus()




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

website_entry = Entry(width=47)
website_entry.grid(column=1, row=1, columnspan=2, sticky="ew", padx=5, pady=5)
website_entry.focus()
email_entry = Entry(width=47)
email_entry.grid(column=1, row=2, columnspan=2, sticky="ew", padx=5, pady=5)
email_entry.insert(0,"jeeva1234@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, columnspan=1, sticky="ew", padx=5, pady=5)

generate_pass_button = Button(text="Generate password",command=generate_password)
generate_pass_button.grid(column=2, row=3, sticky="ew", padx=5, pady=5)

add_button = Button(text="Add", width=40,command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew", padx=5, pady=5)

window.mainloop()
