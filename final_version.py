from tkinter import *
from functools import partial  # To prevent unwanted windows
from tkinter import messagebox as mb
import json
import random


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
                                                  "or if you want to stop playing, press 'quit'...",
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
        self.instruction_frame = Frame(self.quiz_frame)
        self.instruction_frame.grid(row=4, pady=10)

        # for now won't use history button (no, command=ans_history)
        self.ans_hist_button = Button(self.instruction_frame, font=("Calibri", 12, "bold"),
                                       text="Answer History", bg="lightgoldenrod",
                                      width=14)
        self.ans_hist_button.grid(row=0, column=0)


        self.help_button = Button(self.instruction_frame, font=("Calibri", 12, "bold"),
                                  text="Instructions", bg="olivedrab2", command=self.get_help, width=12)
        self.help_button.grid(row=0, column=1)

    def get_to_play(self):
        start_func()
        self.start_button.configure(state=DISABLED) # when opened once, will allow to disabled it again...


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



def start_func():
    # for the questions to display...
    root = Tk()
    root.geometry("550x450")
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
            t = Label(root, text="Maori Aotearoa Place Quiz", width=40, fg="black",
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
            nextbutton.place(x=150, y=380)
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

    PlayQuestion()

class Export:
    def __init__(self, partner, calc_history):
        background = "#a9ef99"  # Pale green

        # disable export button
        partner.export_button.config(state=DISABLED)

        # Sets up child window (export box)
        self.export_box = Toplevel()

        # If users press cross at top, closes export & 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW',
                                 partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, width=300, bg=background)
        self.export_frame.grid()

        # Set up export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export instructions",
                                 font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)

        # Export text (label, row 1)
        self.export_text = Label(self.export_frame,
                                 text="Enter a file name in the box below and "
                                      "press the save button to save your "
                                      "calculation history to a text file",
                                 justify=LEFT, width=40,
                                 bg=background, wrap=250)
        self.export_text.grid(row=2, pady=10)

        # Warning text (label, row 1)
        self.export_text = Label(self.export_frame,
                                 text="If the file name you enter below "
                                      "already exists, it's content will be "
                                      "replaced with your calculation history",
                                 justify=LEFT, font="Arial 10 italic",
                                 bg="#ffafaf",  # Pink
                                 fg="maroon", wrap=225, padx=10, pady=10)
        self.export_text.grid(row=1)

        # Filename entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Save / Cancel Frame (row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon",
                                      bg=background)
        self.save_error_label.grid(row=4)

        # Save / Cancel Frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and cancel buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  command=partial(lambda: self.save_history
                                  (partner, calc_history)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    command=partial
                                    (self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner, calc_history):
        # Has expression to check file name. Can be upper or lower case letters
        valid_char = "[A-Za-z0-9_]"  # Letters or underscores
        has_error = "no"

        filename = self.filename_entry.get()

        for letter in filename:
            if re.match(valid_char, letter):
                continue  # If the letter is valid, goes back and checks next

            elif letter == " ":  # Otherwise, find problems
                problem = "(no spaces allowed)"
            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":  # Describe problem
            self.save_error_label.config(text=f"Invalid filename - {problem}")
            # Change entry box background to light red
            self.filename_entry.config(bg="#ffafaf")
        else:
            # If there are no errors, generate text file and then close
            # Dialogue. Add .txt suffix!

            filename += ".txt"

            # create file to hold data
            f = open(filename, "w+")

            # add new line at end of each item
            for item in calc_history:
                f.write(item + "\n")

            # close file
            f.close()

            # Close dialogue
            self.close_export(partner)

    def close_export(self, partner):
        # Put export button back to normal...
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Menu")
    something = MaoriQuiz()
    root.mainloop()
    root.resizeable = (False, False) # to not resize the GUI's...
