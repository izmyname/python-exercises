import tkinter as tk
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Fira Code Nerd Font Mono"
flip = None
random_pair = {}

# LOAD THE CORRECT FILE
try:
    french_dataframe = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    french_dataframe = pd.read_csv("./data/french_words.csv")


french_dict = french_dataframe.to_dict(orient='records')

# CREATE FLASH CARDS
def flash_card():
    
    global flip, random_pair
    
    if flip != None:
        window.after_cancel(flip)
        canvas.itemconfig(canvas_image, image=front_img)
        
    random_pair = random.choice(french_dict)
    random_pair_fr = random_pair["French"]
    random_pair_en = random_pair["English"]
    canvas.itemconfig(language_name, text="French", fill = "#000000")
    canvas.itemconfig(language_word, text=random_pair_fr, fill = "#000000")

    def flash_card_reverse():
        canvas.itemconfig(canvas_image, image=back_img)
        canvas.itemconfig(language_name, text="English", fill="white")
        canvas.itemconfig(language_word, text=random_pair_en, fill="white")
    
    flip = window.after(3000, flash_card_reverse)
    
    
# HANDLE RIGHT ANSWER

def right_answer():
    flash_card()
    french_dict.remove(random_pair)
    tolearn = pd.DataFrame(french_dict)
    tolearn.to_csv("./data/words_to_learn.csv", index=False)

# CREATE UI

# Create a window
window = tk.Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# Create canvas
canvas = tk.Canvas(width=800,height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# Images
front_img = tk.PhotoImage(file="./images/card_front.png")
back_img = tk.PhotoImage(file="./images/card_back.png")
right = tk.PhotoImage(file="./images/right.png")
wrong = tk.PhotoImage(file="./images/wrong.png")
canvas_image = canvas.create_image(400, 263, image=front_img)

# text
language_name = canvas.create_text(400, 150, text="title",font=(FONT, 40, "italic"))
language_word = canvas.create_text(400, 260, text="Word",font=(FONT, 41, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

# Buttons
right_button = tk.Button(image=right, command=right_answer)
right_button.grid(column=1, row=1)

wrong_button = tk.Button(image=wrong, command=flash_card)
wrong_button.grid(column=0, row=1)

flash_card() # execute this on a program startup to avoid using placeholder first
window.mainloop()

