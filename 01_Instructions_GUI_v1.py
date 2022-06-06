"""01_Instructions_GUI_v1
Creating a basic Interface to test out popping the window open...
Created by Kent Nago
"""

from tkinter import *
import random


class MaoriQuiz: # example window display
    def __init__(self, parent):
        print("Hello World")

        # formatting variables...
        background_color = "deep sky blue" # color change to background

        # quiz main screen GUI...
        self.quiz_frame = Frame(width=300, height=300, bg=background_color) # can use height=300, width=30,
        # but can be deleted, so the text can fit in the box
        self.quiz_frame.grid()

        # maori quiz heading
        self.quiz_label = Label(text="Maori Aotearoa Place Quiz",
                                          font=("Calibri", 14 ,"bold"),
                                          bg=background_color,
                                          padx=10, pady=10)

        self.quiz_label.grid(row=0) 


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Aotearoa Place Quiz")
    something = MaoriQuiz(root)
    root.mainloop()
