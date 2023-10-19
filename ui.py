from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WIDTH = 300
HEIGHT = 250

current_score = 0


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        check_image = PhotoImage(file="../quizzler-app-start/images/true.png")
        x_image = PhotoImage(file="../quizzler-app-start/images/false.png")

        self.button1 = Button(image=check_image, highlightthickness=0, borderwidth=0, command=self.true_pressed)
        self.button1.grid(column=0, row=2, pady=20)

        self.button2 = Button(image=x_image, highlightthickness=0, borderwidth=0, command=self.false_pressed)
        self.button2.grid(column=1, row=2, pady=20)

        self.score = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white", font=("Arial", 10, "bold"))
        self.score.grid(column=1, row=0, pady=20)

        self.canvas = Canvas()
        self.text = self.canvas.create_text(WIDTH/2, HEIGHT/2, width=280, text="filler", font=("Arial", 20, "italic"))
        self.canvas.config(width=WIDTH, height=HEIGHT, bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
            self.score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.text, text="You've reached the end of the quiz")
            self.button1.config(state="disabled")
            self.button2.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)





