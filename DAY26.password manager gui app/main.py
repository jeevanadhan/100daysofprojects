from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------ #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("PASSWORD MANAGER")
window.config(padx=20,pady=20)


canvas=Canvas(width=200,height=224,highlightthickness=0)
photoimage=PhotoImage(file="logo.png")
canvas.create_image(60,112,image=photoimage)
canvas.grid(row=0,column=1)
website_text=Label(text="website:", font=("Arial", 10, "bold"))
website_text.grid(column=0,row=4)
website_text.config(pady=10)
website_entry=Entry(width=50)
website_entry.grid(column=1,row=4,columnspan=2)
email_text=Label(text="Email/Username:", font=("Arial", 10, "bold"))
email_text.grid(column=0,row=5)
email_entry=Entry(width=50)
email_entry.grid(column=1,row=5,columnspan=2)
password_text=Label(text="password:", font=("Arial", 10, "bold"))
password_text.grid(column=0,row=6)
password_entry=Entry(width=21)
password_entry.grid(column=1,row=6,columnspan=2)
password_text.config(pady=10)
generate_pass_button=Button(text="Generate password")
generate_pass_button.grid(column=1,row=6)


window.mainloop()