import tkinter as tk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Fira Code Nerd Font Mono"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_go = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer_go)
    timer.config(text="Timer")
    check.config(text="")
    canvas.itemconfig(timer_count, text="00:00")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    reps += 1

    if reps == 8:
        countdown(long_break_sec)
        timer.config(text="Long break",fg=RED)
    elif reps % 2 == 1:
        countdown(work_sec)
        timer.config(text="Work", fg=GREEN)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer.config(text="Short break", fg=PINK)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    
    count_min = math.floor(count/60)
    count_sec = count % 60
    marks = ""    
    
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_count, text=f"{count_min}:{count_sec}")
    if count >0:
        global timer_go
        timer_go = window.after(1000, countdown, count -1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓ "
        check.config(text=marks)
                

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Tiling compositors have no titlebars")
window.config(padx=100, pady=50, bg=YELLOW)

window.after(1000, )

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = tk.PhotoImage(file='tomato.png')
canvas.create_image(100,112, image=tomato)
timer_count = canvas.create_text(100,130, text="00:00", fill =YELLOW, font=(FONT_NAME, 20, "bold"))
canvas.grid(column=1, row=1)

timer = tk.Label(fg=GREEN, bg=YELLOW, text="Timer", font=(FONT_NAME,32,"normal"))
timer.grid(column=1, row=0)

check = tk.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 16, "normal"))
check.config(pady=20)
check.grid(column=1, row=3)

start = tk.Button(text="Start", highlightthickness=0,  command=start_timer)
start.grid(column=0, row=2)

start = tk.Button(text="Reset", highlightthickness=0, command=reset_timer)
start.grid(column=2, row=2)

window.mainloop()