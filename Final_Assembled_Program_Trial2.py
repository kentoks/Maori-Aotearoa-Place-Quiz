"""Final_Assembled_Program_Trial2
Compiled Program
Following my usability testing and commencing this to
post usability testing...
Program has become short, but meets the requirement for testing...
Created by Kent Nago
"""

from tkinter import *
from tkinter import messagebox as mb
import json
import random
import tkinter as tk


root = Tk()
root.geometry("510x450")
root.title("Maori Aotearoa Place Quiz")

with open('questions2.json') as f:
    obj = json.load(f)
questions = (obj['questions']) # load the questions from JSON file
options = (obj['options']) # load the options from JSON file
answers = (obj['answers']) # load the answers from JSON file
z = zip(questions, options, answers) # matches the questions and options
# and answers in 1 question
l = list(z)
random.shuffle(l)
questions, options, answers = zip(*l)


class PlayQuestion:
    def __init__(self):
        self.qn = 0 # initially setting question = 0
        self.option_selected = IntVar()
        self.optn = self.radio_btns() # the 4 optional radio buttons from questions.
        self.ques = self.question(self.qn)
        self.display_options(self.qn)
        self.buttons()
        self.correct = 0
        self.instructions_label = tk.Label(root, text="Answer the following "
                                                      "questions about the "
                                                      "cities \n"
                                                      "in New Zealand in"
                                                      " Maori. After you have"
                                                      " finished, \n"
                                                      "push 'Next'...",
                                           width=10, fg="Red", padx=40,
                                           pady=30,
                                           font=("Calibri", 10, "underline"))
        self.instructions_label.place(x=100, y=50, relwidth=0.6)

    def question(self, qn):
        quizheading = Label(root, text="Maori Aotearoa Place Quiz", width=37,
                            fg="white", bg="black",
                            font=("Calibri", 20, "bold"), justify=CENTER)

        quizheading.place(x=0, y=3)
        qn = Label(root, text=questions[qn], width=60,
                   font=("Calibri", 16, "italic", "bold"), anchor="w")
        qn.place(x=80, y=150)
        return qn

    def radio_btns(self): # the radio button function
        values = 0
        list = []
        yposition = 200 # the position of the spaces between the radio buttons
        while values < 4: # the number of radio buttons must not exceed 4.
            btn = Radiobutton(root, text="", variable=self.option_selected,
                              value=values+1, font=("Calibri", 14))
            list.append(btn)
            btn.place(x=100, y=yposition)
            values += 1
            yposition += 35
        return list

    def display_options(self, qn):
        values = 0 # initial list value is 0
        self.option_selected.set(0) # or None
        self.ques['text'] = questions[qn]
        for op in options[qn]:
            self.optn[values]['text'] = op
            values += 1

    def buttons(self):  # and adding buttons for next and quits.
        nextbutton = Button(root, text="Next", command=self.next_btn,
                            width=10, bg="Green", fg="white",
                            font=("Calibri", 14, "bold"))
        nextbutton.place(x=80, y=380) # placing them on same y-axis

        quit_button = Button(root, font=("Calibri", 14, "bold"),
                             text="Quit", bg="Red", fg="white",
                             command=root.destroy, width=12)
        quit_button.place(x=300, y=380) # placing them on same y-axis

    def check_ans(self, qn):
        # checking answer function
        if self.option_selected.get() == answers[qn]: # it checks whether it is correct or not
            return True

    def next_btn(self): # next button clickings...
        if self.check_ans(self.qn):
            self.correct += 1
        self.qn += 1
        if self.qn == len(questions):
            self.display_results()
        else:
            self.display_options(self.qn)

    def display_results(self): # displaying results
        score = int(self.correct / len(questions) * 100) # calculates result
        result = "Results: " + str(score) + "%" # displaying result on messagebox
        wc = len(questions) - self.correct # calculates number of incorrect answers
        correct = "Numbers of correct answers: " + str(self.correct)
        incorrect = "Numbers of incorrect answers: " + str(wc)
        mb.showinfo("Result", "\n".join([result, correct, incorrect])) # messagebox title


PlayQuestion() # calling the class
root.mainloop()
