from tkinter import *
from functools import partial  # To prevent unwanted windows
import random



class MaoriQuiz:
    def __init__(self):

        # Formatting variables
        background_color = "deep sky blue"

        # Converter Frame
        self.quiz_frame = Frame(width=300, bg=background_color, pady=10)
        self.quiz_frame.grid()

        # Temperature Converter Heading (row 0)
        self.temp_heading_label = Label(self.quiz_frame,
                                        text="Maori Aotearoa Place Quiz",
                                        font=("Calibri", 16, "bold"),
                                        bg=background_color, padx=10, pady=10)
        self.temp_heading_label.grid(row=0)

        # User instructions (row 1)
        self.temp_instructions_label = Label(self.quiz_frame,
                                             text="Answer the following questions.json about "
                                                  "the cities in New Zealand in Maori."
                                                  " After you have finished, push 'Next'...",
                                             font=("Calibri", 10, "italic"), wrap=250,
                                             justify=LEFT, bg=background_color,
                                             padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)

        # entry box to enter answers (row 2)
        self.entry_box =Entry(self.quiz_frame, width=20,
                                      font=("Calibri", 14, "bold"))
        self.entry_box.grid(row=2)

        # Conversion buttons frame (row 3), khaki1
        self.next_button_frame = Frame(self.quiz_frame)
        self.next_button_frame.grid(row=3, pady=10)

        self.nxt_button = Button(self.next_button_frame,
                                  text="Next", font=("Calibri", 10, "underline"),
                                  bg="Khaki1", padx=10, pady=10)
        self.nxt_button.grid(row=0, column=0)


        # Answer label (row 4)
        self.converted_label = Label(self.quiz_frame, font=("Calibri", 14, "bold"),
                                     fg="black", bg=background_color, pady=10,
                                     text="")
        self.converted_label.grid(row=4)

        # History / Help button frame (row 5)
        self.hist_help_frame = Frame(self.quiz_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        self.ans_hist_button = Button(self.hist_help_frame, font=("Calibri", 12, "bold"),
                                       text="Answer History", width=14)
        self.ans_hist_button.grid(row=0, column=0)

        self.help_button = Button(self.hist_help_frame, font=("Calibri", 12, "bold"),
                                  text="Instructions", width=12)
        self.help_button.grid(row=0, column=1)

# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Aotearoa Place Quiz")
    something = MaoriQuiz()
    root.mainloop()
