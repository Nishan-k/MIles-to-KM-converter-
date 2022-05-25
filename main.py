from tkinter import *

# TODO 1: Create the window and set the title:
window = Tk()
window.title("Mile to KM Converter.")
window.minsize(width=400, height=250)
window.config(padx=60, pady=70)
# TODO 2: Create label and button for Miles:
mile_entry = Entry(width=15)
mile_entry.grid(row=0, column=1)
label_miles = Label(text="Miles", font=("Arial", 14))
label_miles.grid(row=0, column=2)
label_miles.config(padx=10)
# TODO 3: Result area:
result_label = Label(text="is equal to: ", font=("Arial", 14))
result_label.grid(row=2, column=0)
result_label.config(pady=10)
km_output_label = Label(text="0", font=("Arial", 14))
km_output_label.grid(row=2, column=1)
km_output_label.config(pady=10)
km_label = Label(text="Km", font=("Arial", 14))
km_label.grid(row=2, column=2)


# TODO 4: Function that converts miles to KM and displays the result:
def convert_value():
    value = int(mile_entry.get())
    km_output_label["text"] = round(value * 1.609,2)


# TODO 5: Button to convert Miles to KM:
button = Button(text="Convert", width=12, height=2, command=convert_value)
button.grid(row=3, column=1)

window.mainloop()
