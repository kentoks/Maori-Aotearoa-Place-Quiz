"""04_temporaryQuiz_v2_Trial2
It is copied form 04_temporaryQuiz_v1 and made the following refinements...
I have added a statistics to record the number of correct answers and wrong answers
I have randomised the questions...
Created by Kent Nago
"""

from tkinter import *
from tkinter import messagebox as mb
import json
import random


root = Tk()
root.geometry("550x450")
root.title("Maori Aotearoa Place Quiz")

with open('questions2.json') as f:
    obj = json.load(f)
questions = (obj['questions'])
options = (obj['options'])
answers = (obj['answers'])
z = zip(questions,options,answers)
l = list(z)
random.shuffle(l)
questions,options,answers=zip(*l)
print(questions)
print(options)
print(answers)

class PlayQuestion:
    def __init__(self):
        self.qn = 0
        self.option_selected = IntVar()
        self.optn = self.radio_btns()
        self.ques = self.question(self.qn)
        self.display_options(self.qn)
        self.buttons()
        self.correct = 0


    def question(self, qn):
        t = Label(root, text="Maori Aotearoa Place Quiz", width=40, fg="white",bg="black",
                    font=("Calibri", 20, "bold"))
        t.place(x=0, y=2)
        qn = Label(root, text=questions[qn], width=60, font=("Calibri", 16, "italic"), anchor="w")
        qn.place(x=70, y=100)
        return qn

    def radio_btns(self):
        values = 0
        list = []
        yp = 150
        while values < 4:
            btn = Radiobutton(root, text="", variable=self.option_selected,
                                value= values + 1, font=("Calibri", 14))
            list.append(btn)
            btn.place(x=100, y=yp)
            values += 1
            yp += 40
        return list

    def display_options(self, qn):
        values = 0
        self.option_selected.set(0)
        self.ques['text'] = questions[qn]
        for op in options[qn]:
            self.optn[values]['text'] = op
            values +=1

    def buttons(self):
        nextbutton = Button(root, text="Next", command=self.next_btn, width=10, bg="green", fg="white",
                            font=("Calibri", 16, "bold"))
        nextbutton.place(x=100, y=380)
        quitbutton = Button(root, text="Quit", command=root.destroy, width=10, bg="red", fg="white",
                            font=("Calibri", 16, "bold"))
        quitbutton.place(x=300, y=380)

    def check_ans(self, qn):
        if self.option_selected.get() == answers[qn]:
            return True

    def next_btn(self):
        if self.check_ans(self.qn):
            self.correct += 1
        self.qn += 1
        if self.qn == len(questions):
            self.display_results()
        else:
            self.display_options(self.qn)

    def display_results(self):
        score = int(self.correct / len(questions) * 100)
        result = "Results: " + str(score) + "%"
        wc = len(questions) - self.correct
        correct = "Numbers of correct answers: " + str(self.correct)
        incorrect = "Numbers of incorrect answers: " + str(wc)
        mb.showinfo("Result", "\n".join([result, correct, incorrect]))

quiz = PlayQuestion()
root.mainloop()
