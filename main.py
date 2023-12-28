from tkinter import *

window = Tk()
window.title("Distance Convertor")
window.config(padx=20, pady=20)

def miles_to_km():
    if mile_entry.get() == "":
        pass
    else:
        mile = float(mile_entry.get())
        km = round(mile*1.609344,2)
        answer_label.config(text=f"{km}", justify="right", anchor="e")


mile_entry = Entry()
mile_entry.config(width=7, justify="right")
mile_entry.grid(column=2, row=1)

mile_label = Label()
mile_label.config(text="Miles")
mile_label.grid(column=3, row=1)

equal_label  = Label()
equal_label.config(text="is equal to")
equal_label.grid(column=1, row=2)

answer_label = Label()
answer_label.config(text="0", width=8, anchor="e", justify="right")
answer_label.grid(column=2, row=2)

km_label = Label()
km_label.config(text="Km")
km_label.grid(column=3, row=2)

calculate = Button(command=miles_to_km)
calculate.config(text="Calculate")
calculate.grid(column=2, row=3)



window.mainloop()

