import tkinter as tk

window = tk.Tk()
window.title("you can see it only in hyprctl clients output")
window.minsize(800,600)

my_label = tk.Label(text = "Hello there", font=("Fira Code Nerd Mono", 28, "bold"))
my_label.grid(column = 0, row = 0)

def click_button():
    my_label.config(text=f"{input.get()}")

def get_a_kitten():
    my_label.config(text=f"No kitten for you!")

button = tk.Button(text="Launch nuclear missiles", command = click_button)
button.grid(column = 1, row = 1)

button = tk.Button(text="Give me a kitten", command = get_a_kitten)
button.grid(column = 2, row = 0)

input = tk.Entry(width=12)
input.grid(column = 3, row =2)

window.mainloop()

