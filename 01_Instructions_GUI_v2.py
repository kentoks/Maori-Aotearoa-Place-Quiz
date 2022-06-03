from tkinter import *
from functools import partial  # To prevent unwanted windows

import random


class MaoriQuiz:
    def __init__(self):

        # Formatting variables...
        background_color = "deep sky blue"

        # Maori Quiz Frame
        self.quiz_frame = Frame(width=300, height=300, bg=background_color, pady=10)
        self.quiz_frame.grid()

        # The quiz Heading (row 0)
        self.quiz_heading_label = Label(self.quiz_frame,
                                          text="Maori Aotearoa Place Quiz",
                                          font=("Calibri", 16, "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.quiz_heading_label.grid(row=0)

        # Instructions Button (row 1)
        self.instructions_button = Button(self.quiz_frame, text="Instructions", font=("Calibri", 12),
                                  padx=20, pady=10, command=self.instructions)
        self.instructions_button.grid(row=1)

    def instructions(self):
        print("You have asked for Instructions")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Aotearoa Place Quiz")
    something = MaoriQuiz()
    root.mainloop()
