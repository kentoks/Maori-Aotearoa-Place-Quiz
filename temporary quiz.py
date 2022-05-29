# will be adding a footer frame to make my interface prettier (later on in improvements)
# does not display history button at the moment
# this quiz can save the previous answer, so that no questions are missed

from tkinter import *
from functools import partial  # To prevent unwanted windows
import random
import json
from tkinter import messagebox as mb


class MaoriQuiz:
    def __init__(self):

        # Formatting variables
        background_color = "deep sky blue"

        # Main Quiz Frame
        self.quiz_frame = Frame(width=300, bg=background_color, pady=10)
        self.quiz_frame.grid()

        # Maori Quiz Heading (row 0)
        self.quiz_heading_label = Label(self.quiz_frame,
                                        text="Maori Aotearoa Place Quiz",
                                        font=("Calibri", 16, "bold"),
                                        bg=background_color, padx=10, pady=10)
        self.quiz_heading_label.grid(row=0)

        # User beginning (row 1)
        self.user_beginning_label = Label(self.quiz_frame,
                                             text="Remember that this quiz for fun... "
                                                  "If you are stuck, press 'help' below "
                                                  "or if you want to export history, press"
                                                  " 'Answer History'",
                                             font=("Calibri", 10, "italic"), wrap=250,
                                             justify=LEFT, bg=background_color,
                                             padx=10, pady=10)
        self.user_beginning_label.grid(row=1)

        # Button to start playing (not functional at the moment) (row 2)
        self.start_button =Button(self.quiz_frame, text="Start", width=15,
                                      font=("Calibri", 14, "bold"),
                                  bg="honeydew1", command=self.get_to_play, padx=5, pady=10)
        self.start_button.grid(row=2)


        # label to make user press start (row 3)
        self.answer_label = Label(self.quiz_frame, font=("Calibri", 16, "underline"),
                                  fg="red",bg=background_color, pady=10,
                                  text="press 'Start' to begin!!")
        self.answer_label.grid(row=3)


        # History / Instructions button frame (row 4)
        self.hist_instruction_frame = Frame(self.quiz_frame)
        self.hist_instruction_frame.grid(row=4, pady=10)

        # for now won't use history button (no, command=ans_history)
        self.ans_hist_button = Button(self.hist_instruction_frame, font=("Calibri", 12, "bold"),
                                       text="Answer History", bg="lightgoldenrod",
                                      width=14)
        self.ans_hist_button.grid(row=0, column=0)

        self.help_button = Button(self.hist_instruction_frame, font=("Calibri", 12, "bold"),
                                  text="Instructions", bg="olivedrab2", command=self.get_help, width=12)
        self.help_button.grid(row=0, column=1)

    def get_to_play(self):
        start_func()

    def get_help(self):
        help = Instructions(self)
        help.instructions_text.configure(text="Answer the following questions about the cities "
                                              "in New Zealand in Maori."" After you have finished, "
                                              "push 'Next'...")


class Instructions:
    def __init__(self, partner):

        background = "olivedrab2"

        # disable instructions button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (instructions box)
        self.instructions_box = Toplevel()

        # If users press cross at top, closes instructions and 'releases' instructions button
        self.instructions_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_instructions, partner))

        # Set up GUI Frame
        self.instructions_frame = Frame(self.instructions_box, width=300, bg=background)
        self.instructions_frame.grid()

        # Set up instructions heading (row 0)
        self.how_heading = Label(self.instructions_frame, text="Instructions",
                                    font=("Calibri", 15, "bold"), bg=background)
        self.how_heading.grid(row=0)

        # instructions text (label, row 1)
        self.instructions_text = Label(self.instructions_frame, text="", font=("Calibri", 9, "italic"),
                               justify=LEFT, width=45, bg=background, wrap=250)
        self.instructions_text.grid(row=1)

        # Close button (row 2)
        self.close_btn = Button(self.instructions_frame, text="Close",
                                  width=10, bg="olivedrab2", font=("Calibri", 10, "bold"),
                                  command=partial(self.close_instructions, partner))
        self.close_btn.grid(row=2, pady=10)

    def close_instructions(self, partner):
        # Put instructions button back to normal..
        partner.help_button.config(state=NORMAL)
        # close the window
        self.instructions_box.destroy()

# class History:
#     def __init__(self):


def start_func():
    # for the questions to display...

    root = Tk()
    root.geometry("650x450")
    root.title("Quiz")

    with open('questions2.json') as f:
        obj = json.load(f)
    questions = (obj['questions'])
    options = (obj['options'])
    answers = (obj['answers'])
    z = zip(questions,options,answers)
    l = list(z)
    random.shuffle(l)
    questions,options,answers=zip(*l)

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
            t = Label(root, text="Playing quiz", width=40, fg="black",
                      font=("Times", 20, "bold"))
            t.place(x=0, y=2)
            qn = Label(root, text=questions[qn], width=60, font=("Times", 16, "bold"), anchor="w")
            qn.place(x=70, y=100)
            return qn

        def radio_btns(self):
            values = 0
            b = []
            yp = 150
            while values < 4:
                btn = Radiobutton(root, text="", variable=self.option_selected,
                                  value = values + 1, font=("Times", 14))
                b.append(btn)
                btn.place(x=100, y=yp)
                values += 1
                yp += 40
            return b

        def display_options(self, qn):
            values = 0
            self.option_selected.set(0)
            self.ques['text'] = questions[qn]
            for op in options[qn]:
                self.optn[values]['text'] = op
                values +=1

        def buttons(self):
            nextbutton = Button(root, text="Next", command=self.next_btn, width=10, bg="green", fg="white",
                             font=("Times", 16, "bold"))
            nextbutton.place(x=150, y=380)
            quitbutton = Button(root, text="Quit", command=root.destroy, width=10, bg="red", fg="white",
                                font=("Times", 16, "bold"))
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


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Aotearoa Place Quiz")
    something = MaoriQuiz()
    root.mainloop()

