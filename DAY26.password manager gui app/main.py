from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("PASSWORD MANAGER")
window.config(padx=20,pady=20)


canvas=Canvas(width=200,height=224,highlightthickness=0)
photoimage=PhotoImage(file="logo.png")
canvas.create_image(100,112,image=photoimage)
canvas.grid(row=0,column=1)
.

window.mainloop()