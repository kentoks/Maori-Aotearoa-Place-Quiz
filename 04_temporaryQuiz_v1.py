"""04_temporaryQuiz_v1
It is only the PlayQuestion GUI, where it displays the questions
In order from Questions 1-10
Have made the program so that users must click 'quit' to finish...
Created by Kent Nago
"""

from tkinter import *
import json



root = Tk()
root.geometry("550x450")
root.title("Maori Aotearoa Place Quiz")

with open('questions.json') as f:
    obj = json.load(f)
questions = (obj['questions']) # load the questions from JSON file
options = (obj['options']) # load the options from JSON file
answers = (obj['answers']) # load the answers from JSON file
print(questions) 
print(options)
print(answers)

class PlayQuestion: # PlayQuestion class to run the quiz...
    def __init__(self):
        self.qn = 0 # initially setting question = 0
        self.option_selected = IntVar()
        self.optn = self.radio_btns() # the 4 optional radio buttons from questions.
        self.ques = self.question(self.qn)
        self.display_options(self.qn)
        self.buttons() # buttons for next, quit buttons...
        self.correct = 0


    def question(self, qn):
        t = Label(root, text="Maori Aotearoa Place Quiz", width=40, fg="white",bg="black",
                    font=("Calibri", 20, "bold"))
        t.place(x=0, y=2)
        qn = Label(root, text=questions[qn], width=60, font=("Calibri", 16, "italic"), anchor="w")
        qn.place(x=70, y=100)
        return qn

    def radio_btns(self): # the radio button function
        values = 0
        list = []
        yposition = 150 # the position of the spaces between the radio buttons
        while values < 4: # the number of radio buttons must not exceed 4.
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
            print("") # must let user to click 'Quit' to finish...
        else:
            self.display_options(self.qn)

    # display results

quiz = PlayQuestion()
root.mainloop()
