import tkinter as tk
from quiz_brain import  QuizBrain

THEME_COLOR = "#375362"
FONT = "Arial"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzer")
        self.window.configure(padx=20,pady=20,bg=THEME_COLOR)
        self.canvas()
        self.false_button()
        self.true_button()
        self.score()
        self.get_next_question()
        
        self.window.mainloop()
        
    def canvas(self):
        self.canvas = tk.Canvas(width=300,height=250,bg="white")
        self.question_text = self.canvas.create_text(150,125,text="the question", width = 280, font=(FONT, 20, "italic"))
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)
    
    def score(self):
        self.score = tk.Label(text=f"Score: {self.quiz.score}")
        self.score.config(bg=THEME_COLOR,fg="white")
        self.score.grid(column=1,row=0)
    
    def false_button(self):
        self.wrong_image = tk.PhotoImage(file="./images/false.png")
        self.false_button = tk.Button(image=self.wrong_image,command=self.false_answer)
        self.false_button.config(pady=50,highlightthickness=0)
        self.false_button.grid(column=1,row=2)
    
    def true_button(self):
        self.right_image = tk.PhotoImage(file="./images/true.png")
        self.true_button = tk.Button(image=self.right_image,command=self.true_answer)
        self.true_button.config(pady=50,highlightthickness=0)
        self.true_button.grid(column=0,row=2)
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="The quiz is over" )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        
    def true_answer(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    
    def false_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)