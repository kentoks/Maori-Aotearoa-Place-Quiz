from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class MaoriQuiz:
    def __init__(self):

        # Formatting variables
        background_color = "deep sky blue"

        # Frame
        self.question_frame = Frame(width=300, bg=background_color, pady=10)
        self.question_frame.grid()

        # The quiz Heading (row 0)
        self.quiz_label = Label(self.question_frame,
                                        text="Maori Aotearoa Place Quiz",
                                        font=("Calibri", 16, "bold"),
                                        bg=background_color, padx=10, pady=10)
        self.quiz_label.grid(row=0)


        # User instructions (row 1)
        self.quiz_instruction_label = Label(self.question_frame,
                                             text="Instructions...",
                                             font=("Calibri", 10, "italic"), wrap=250,
                                             justify=LEFT, bg=background_color,
                                             padx=10, pady=10)
        self.quiz_instruction_label.grid(row=1)

        # Start button and side window (row 2)

        # button Frame (Row 1)
        self.buttons = Frame(self.question_frame, width=100, height=100, bg=background_color)
        self.buttons.grid(row=2)


        # Start Button creation (row 2)
        self.make_buttons = Button(self.buttons,
                                 text="Start",
                                 width=10, height=1,
                                 padx=10, pady=10,
                                 command=self.answers)
        self.make_buttons.grid(row=2)

    def answers(self): 
        x = QuizInterface(self)


# Quiz interface GUI
class QuizInterface:

    # Initializing the Function
    def __init__(self, menu):
        # Formatting Variables
        bg_colour = "orange" # change color later...

        # Disable/Closing Button in Menu
        menu.make_buttons.configure(state=DISABLED)

        # Create new Window
        self.new_window = Toplevel()
        self.new_window.protocol('WM_DELETE_WINDOW', partial(self.make_close, menu))

        # Main Frame
        self.main_frame = Frame(self.new_window, width=100, height=100, bg=bg_colour)
        self.main_frame.grid()

        # heading (row 0)
        self.label_heading = Label(self.main_frame,
                                   text="Questions...",
                                   font=("Calibri", 16, "bold"),
                                   bg=bg_colour,
                                   padx=10, pady=10, width=15, height=2) # for now these settings...
        self.label_heading.grid(row=0) 


        # Footer Frame (Row 2)
        self.main_frame_footer = Frame(self.main_frame, width=100, height=20, bg=bg_colour)
        self.main_frame_footer.grid(row=2)


        # Dismiss Button (row 0)
        self.closing = Button(self.main_frame_footer,
                                 text="Dismiss",
                                 width=10, height=2,
                                 padx=1, pady=1,
                                 command=partial(self.make_close, menu))
        self.closing.grid(row=0)

    def make_close(self, menu):
        menu.make_buttons.configure(state=NORMAL)

        # close Window
        self.new_window.destroy()


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Aotearoa Place Quiz")
    something = MaoriQuiz()
    root.mainloop()
