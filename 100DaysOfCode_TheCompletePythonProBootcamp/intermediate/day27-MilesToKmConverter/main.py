import tkinter as tk

# Function for a button to do magic
def miles_to_km():
    return kms_display.config(text = f"{round((float(miles_entry.get()) * 1.609344), 2)}") if not miles_entry.get() == "" else 0

# configure screen
gui = tk.Tk()
gui.title("Miles to km converter")
gui.minsize(200,100)
gui.config(padx = 10, pady = 20)

# insert miles int here
miles_entry = tk.Entry(width = 5)
miles_entry.grid(column = 1, row = 0)

# Miles
miles_label = tk.Label(text="Miles")
miles_label.grid(column = 2, row = 0)

# is equal to
equal_label = tk.Label(text="is equal to ")
equal_label.grid(column = 0, row = 1)

# Output kilometers here
kms_display = tk.Label(text="0")
kms_display.grid(column = 1, row = 1)

# Km
kms_label = tk.Label(text="Km")
kms_label.grid(column = 2, row = 1)

# Button
calculate = tk.Button(text = "Calculate", command = miles_to_km)
calculate.grid(column = 1, row = 2)

gui.mainloop()