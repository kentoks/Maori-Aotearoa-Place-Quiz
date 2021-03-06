"""01_Instructions_GUI_v5
Fully functional and working 'Instructions GUI'
Created by Kent Nago
"""

from tkinter import *
from functools import partial  # To prevent unwanted windows

import random # not going to be used for now...


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
        get_help = Instructions(self)
        get_help.instructions_text.configure(text="Instructions text goes here") # what does it do?


class Instructions:
    def __init__(self, partner):
        background = "olivedrab2"

        # sets up child window (ie: help box)
        self.help_box = Toplevel()

        # disable 'help' button
        partner.instructions_button.config(state=DISABLED) # just for now disable the instruction button...

        # sets up GUI frame
        self.instructions_frame = Frame(self.help_box, width=300, bg=background)
        self.instructions_frame.grid()

        # sets up help heading (row 0) (1st row)
        self.how_heading = Label(self.instructions_frame, text="Help/instructions",
                                 font=("Calibri", 12, "bold"), bg=background)
        self.how_heading.grid(row=0)

        # help text (label, row 1) (2nd row)
        self.instructions_text = Label(self.instructions_frame, text="", justify=LEFT,
                               width=40, bg=background, wrap=250)

        self.instructions_text.grid(row=1)

        # Closing button (row 2) (3rd row)
        self.close_button = Button(self.instructions_frame, text="Close", width=10,
                                     bg="olivedrab2", font=("Calibri", 12, "bold"),
                                     command=partial(self.close_instructions, partner))
        self.close_button.grid(row=2, pady=10)

    def close_instructions(self, partner):
        partner.instructions_button.config(state=NORMAL)
        self.help_box.destroy() # closes the help sub interface...


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Aotearoa Place Quiz")
    something = MaoriQuiz()
    root.mainloop()
