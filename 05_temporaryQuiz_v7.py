import random
import json
from tkinter import *
from tkinter import messagebox as mb # displaying the tiny minibox for stats
import tkinter.ttk as ttk
from functools import partial # minimize lot of windows opened
from niggas import *

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
        self.start_button = Button(self.quiz_frame, text="Start", width=15,
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
                                       text="Result History", bg="lightgoldenrod",
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
