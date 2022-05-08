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

        # Maori Quiz Heading (row 0)
        self.quiz_heading_label = Label(self.quiz_frame,
                                          text="Maori Aotearoa Place Quiz",
                                          font=("Calibri", 16, "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.quiz_heading_label.grid(row=0)

        # Instructions Button (row 1)
        self.instructions_button = Button(self.quiz_frame, text="Instructions", font=("Calibri", 14),
                                  padx=10, pady=10, command=self.Instructions)
        self.instructions_button.grid(row=1)

    def Instructions(self):
        print("You asked for Instructions")
        get_instructions = instructions(self)
        get_instructions.instructions_text.configure(text="Instructions text goes here")


class instructions:
    def __init__(self, partner):
        background = "orange" # will color code later on...

        # Sets up child window (instructions box)
        self.instructions_box = Toplevel()

        # Set up GUI Frame
        self.instructions_frame = Frame(self.instructions_box, width=300, bg=background)
        self.instructions_frame.grid()

        # Set up instructions heading (row 0)
        self.how_heading = Label(self.instructions_frame, text="Instructions",
                                 font=("Calibri", 10, "bold"), bg=background)
        self.how_heading.grid(row=0)

        # instructions text (label, row 1)
        self.instructions_text = Label(self.instructions_frame, text="",
                                justify=LEFT, width=40, bg=background, wrap=250)
        self.instructions_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.instructions_frame, text="Dismiss",
                                    width=10, bg="orange", font=("Calibri", 10, "bold"),
                                    command=partial(self.close_instructions, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_instructions(self, partner):
        self.instructions_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Aotearoa Place Quiz")
    something = MaoriQuiz()
    root.mainloop()

