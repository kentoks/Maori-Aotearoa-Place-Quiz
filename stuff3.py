from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class MaoriQuiz:
    def __init__(self):

        # Formatting variables
        background_color = "deep sky blue"

        self.all_answers = ['your results are 60%, no of wrong = 4, no of correct = 6',
                            'your results are 30%, no of wrong = 7, no of correct = 3',
                            'your results are 90%, no of wrong = 1, no of correct = 9']

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
                                             text="In this multi choice quiz you are going"
                                                  "to have to choose the correct English cities for"
                                                  "a certain Maori translated cities",
                                             font=("Calibri", 10, "italic"), wrap=250,
                                             justify=LEFT, bg=background_color,
                                             padx=10, pady=10)
        self.user_beginning_label.grid(row=1)

        # Button to start playing (not functional at the moment) (row 2)
        self.start_button =Button(self.quiz_frame, text="Start", width=15,
                                      font=("Calibri", 14, "bold"),
                                  bg="honeydew1", padx=5, pady=10)
        self.start_button.grid(row=2)

        # label to make user press start (row 3),
        self.answer_label = Label(self.quiz_frame, font=("Calibri", 16, "underline"),
                                  fg="red",bg=background_color, pady=10,
                                  text="press 'Start' to begin!!")
        self.answer_label.grid(row=3)


        # History / Instructions button frame (row 4)
        self.hist_instruction_frame = Frame(self.quiz_frame)
        self.hist_instruction_frame.grid(row=4, pady=10)

        self.ans_hist_button = Button(self.hist_instruction_frame, font=("Calibri", 12, "bold"),
                                       text="Answer History", bg="lightgoldenrod", width=14,
                                      command=lambda: self.history(self.all_answers))
        self.ans_hist_button.grid(row=0, column=0)

        self.help_button = Button(self.hist_instruction_frame, font=("Calibri", 12, "bold"),
                                  text="Instructions", bg="olivedrab2", width=12)
        self.help_button.grid(row=0, column=1)


    def history(self, answer_history):
        History(self, answer_history)

class History:
    def __init__(self, partner, answer_history): # what is partner?
        background = "pale green" # hex code for pale green
        # a9ef99 does not work

        # disable 'history' button
        partner.ans_hist_button.config(state=DISABLED) # what does state mean?

        # sets up child window (ie: history box)
        self.history_box = Toplevel()

        # if users press cross at top, it will close 'history' and and 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_anshistory,
                                                           partner))

        # sets up GUI frame
        self.history_frame = Frame(self.history_box, width=300, bg=background)
        self.history_frame.grid()

        # sets up history heading (row 0) (1st row)
        self.how_heading = Label(self.history_frame, text="Calculation History",
                                 font=("Calibri", 12, "bold"), bg=background)
        self.how_heading.grid(row=0)


        self.history_text = Label(self.history_frame,
                                  text="Here are your most recent calculations"
                                       ". Please use the export button to "
                                       "create a text file of all your "
                                       "calculations for this session",
                                  justify=LEFT, width=40, bg=background,
                                  wrap=250, font=("Calibri", 10, "italic"), fg="maroon",
                                  pady=10, padx=10)
        self.history_text.grid(row=1)


        # history output goes here... (row 2)
        anshistory_string = ""
        if len(answer_history) >= 3:
            # The list must be greater or equal to zero
            # it cannot be greater than the number, since it could not print calculation history
            for item in range (0,3):
                anshistory_string += answer_history[len(answer_history)-item-1] +"\n"

        else:
            for item in answer_history:
                anshistory_string += answer_history[len(answer_history) -
                                                      answer_history.index(item)-1] + "\n"
                self.history_text.config(text="Here is your calculation "
                                              "history: You can use this "
                                              "export button to save this data"
                                              " to a text file if desired.")

        # Label to display calculation history to enter
        self.answer_label = Label(self.history_frame, text=anshistory_string, bg=background,
                                       font=("Calibri", 12), justify=LEFT)
        self.answer_label.grid(row=2)

        # export / dismiss buttons frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # export button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font=("Calibri", 11, "bold"))
        self.export_button.grid(row=0, column=0)

        # dismiss button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     bg="orange", font=("Calibri", 11, "bold"),
                                     command=partial(self.close_anshistory, partner))

        self.dismiss_button.grid(row=0, column=1)

    def close_anshistory(self, partner):
        # put history button back to normal...
        partner.ans_hist_button.config(state=NORMAL) # returns the 'disabled' to 'normal' to make it reopenable
        self.history_box.destroy() # remember about destroy() which is just closing the box

# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Aotearoa Place Quiz")
    something = MaoriQuiz()
    root.mainloop()


