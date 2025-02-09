from tkinter import *
window=Tk()
window.title(string="mile to km converter")
window.config(padx=10,pady=10)
def miles_to_kilo():
    miles=int(miles_input.get())
    kilo=miles * 1.609
    km_result_label.config(text=str(kilo))
mile_label=Label(text="mile", font=("aerial", 10, "bold"))
mile_label.grid(column=2, row=0)
mile_label.config(padx=5, pady=5)

is_equal_to_label=Label(text="is equal to", font=("aerial", 10, "bold"))
is_equal_to_label.grid(column=0, row=2)
is_equal_to_label.config(padx=10, pady=10)

km_label=Label(text="km", font=("aerial", 10, "bold"))
km_label.grid(column=2, row=2)
km_label.config(padx=5, pady=5)

km_result_label=Label(text="0", font=("aerial", 10, "bold"))
km_result_label.grid(column=1, row=2)
km_result_label.config(padx=5, pady=5)

button=Button(text="CALCULATE",command=miles_to_kilo)
button.grid(column=1,row=3)

miles_input=Entry(width=15)
miles_input.grid(column=1,row=0)

window.mainloop()