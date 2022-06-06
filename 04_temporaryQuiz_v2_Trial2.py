"""04_temporaryQuiz_v2_Trial2
It is copied form 04_temporaryQuiz_v2_Trial2
Have only changed the print statements from printing question,options,answers
to a simple, "Good Luck..."
Created by Kent Nago
"""

from tkinter import *
from tkinter import messagebox as mb
import json
import random


root = Tk()
root.geometry("550x450") # setting the geometry to fixed 550x450
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
print("GOOD LUCK...")

class PlayQuestion: # PlayQuestion class to run the quiz...
    def __init__(self):
        self.qn = 0
        self.option_selected = IntVar()
        self.optn = self.radio_btns()
        self.ques = self.question(self.qn)
        self.display_options(self.qn)
        self.buttons()
        self.correct = 0


    def question(self, qn):
        # question function
        t = Label(root, text="Maori Aotearoa Place Quiz", width=40, fg="white",bg="black",
                    font=("Calibri", 20, "bold"))
        t.place(x=0, y=2)
        qn = Label(root, text=questions[qn], width=60, font=("Calibri", 16, "italic"), anchor="w")
        qn.place(x=70, y=100)
        return qn

    def radio_btns(self):
        # radio button function
        values = 0 # initial value = 0
        list = []
        yposition = 150
        while values < 4: # value of radiobuttons can't be greater than 4 buttons...
            btn = Radiobutton(root, text="", variable=self.option_selected,
                                value= values + 1, font=("Calibri", 14))
            list.append(btn)
            btn.place(x=100, y=yposition)
            values += 1
            yposition += 40
        return list

    def display_options(self, qn):
        values = 0
        self.option_selected.set(0)
        self.ques['text'] = questions[qn]
        for op in options[qn]:
            self.optn[values]['text'] = op
            values +=1

    def buttons(self):
        # button function
        nextbutton = Button(root, text="Next", command=self.next_btn, width=10, bg="green", fg="white",
                            font=("Calibri", 16, "bold"))
        nextbutton.place(x=100, y=380)
        quitbutton = Button(root, text="Quit", command=root.destroy, width=10, bg="red", fg="white",
                            font=("Calibri", 16, "bold"))
        quitbutton.place(x=300, y=380)

    def check_ans(self, qn):
        # check answer function
        if self.option_selected.get() == answers[qn]:
            return True

    def next_btn(self):
        # next button function
        if self.check_ans(self.qn):
            self.correct += 1
        self.qn += 1
        if self.qn == len(questions):
            self.display_results()
        else:
            self.display_options(self.qn)

    def display_results(self):
        # display results function
        score = int(self.correct / len(questions) * 100)
        result = "Results: " + str(score) + "%"
        wc = len(questions) - self.correct
        correct = "Numbers of correct answers: " + str(self.correct)
        incorrect = "Numbers of incorrect answers: " + str(wc)
        mb.showinfo("Result", "\n".join([result, correct, incorrect]))

quiz = PlayQuestion()
root.mainloop()
