from tkinter import *
from functools import partial  # To prevent unwanted windows
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
                                       text="Answer History", bg="lightgoldenrod", width=14)
        self.ans_hist_button.grid(row=0, column=0)

        self.help_button = Button(self.hist_instruction_frame, font=("Calibri", 12, "bold"),
                                  text="Instructions", bg="olivedrab2", width=12) # have changed color from
        # lightgoldenrod, so that to avoid confusion.
        self.help_button.grid(row=0, column=1)



# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Aotearoa Place Quiz")
    something = MaoriQuiz()
    root.mainloop()

    
