from tkinter import *
from functools import partial  # To prevent unwanted windows

import random


class Quiz:
    def __init__(self):

        # Formatting variables...
        background_color = "deep sky blue"

        # Quiz Main Screen GUI...
        self.quiz_frame = Frame(width=300, height=300, bg=background_color, pady=10)
        self.quiz_frame.grid()

        # The quiz Heading (row 0)
        self.place_quiz_label = Label(self.quiz_frame,
                                          text="Maori Aotearoa Place Quiz",
                                          font=("Calibri", 16, "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.place_quiz_label.grid(row=0)

        # Help Button (row 1)
        self.help_button = Button(self.quiz_frame, text="Help", font=("Calibri", "14"),
                                  padx=10, pady=10, command=self.help)
        self.help_button.grid(row=1)

    def help(self):
        print("You asked for Help")
        get_help = Help()
        get_help.help_text.configure(text="Help text goes here")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Aotearoa Place Quiz")
    something = Quiz(root)
    root.mainloop()
