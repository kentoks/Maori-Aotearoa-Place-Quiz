from tkinter import *
from functools import partial  # To prevent unwanted windows
import random

def buttons(self): # showing buttons
# The first button is the Next button to move to the
# next Question
    next_button = Button(self.window, text="Next", command=self.next_btn,
                             width=10, bg="green", fg="white", font=("ariel", 16, "bold"))

    # placing the button  on the screen
    next_button.place(x=350, y=460)
