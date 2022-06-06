# will be adding a footer frame to make my interface prettier (later on in improvements)
# does not display history button at the moment

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
                                  bg="honeydew1", command=self.get_to_play, padx=5, pady=10)
        self.start_button.grid(row=2)


        # label to make user press start (row 3)
        self.answer_label = Label(self.quiz_frame, font=("Calibri", 16, "underline"),
                                  fg="red",bg=background_color, pady=10,
                                  text="press 'Start' to begin!!")
        self.answer_label.grid(row=3)


        # History / Instructions button frame (row 4)
        self.hist_instruction_frame = Frame(self.quiz_frame)
        self.hist_instruction_frame.grid(row=4, pady=10)


        self.help_button = Button(self.hist_instruction_frame, font=("Calibri", 12, "bold"),
                                  text="Instructions", bg="lightgoldenrod", command=self.get_help, width=12)
        self.help_button.grid(row=0)

    def get_to_play(self):
        play = PlayQuestion(self)
        play.question_text.configure(text="Questions added later...")

    def get_help(self):
        help = Instructions(self)
        help.instructions_text.configure(text="Answer the following questions about the cities "
                                              "in New Zealand in Maori."" After you have finished, "
                                              "push 'Next'...")


class Instructions:
    def __init__(self, partner):

        background = "lightgoldenrod"

        # disable instructions button...
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
                                  width=10, bg="lightgoldenrod", font=("Calibri", 10, "bold"),
                                  command=partial(self.close_instructions, partner))
        self.close_btn.grid(row=2, pady=10)

    def close_instructions(self, partner):
        # Put instructions button back to normal..
        partner.help_button.config(state=NORMAL)
        # close the window
        self.instructions_box.destroy()


class PlayQuestion:
    def __init__(self, partner):

        background_colour2 = "deep sky blue"

        # disable the 'play' button in the main Maori Quiz Interface
        partner.start_button.configure(state=DISABLED)

        # Set up child window (Question box)
        self.question_box = Toplevel()

        # If users press cross at top, closes instructions and 'releases' instructions button
        self.question_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_question, partner))

        # Set up 2nd GUI Frame
        self.question_frame = Frame(self.question_box, width=300, bg=background_colour2)
        self.question_frame.grid()

        # Set up Question heading (row 0)
        self.how_heading = Label(self.question_frame, text="Welcome...",
                                    font=("Calibri", 15, "bold"), bg=background_colour2)
        self.how_heading.grid(row=0)

        # Question text (label, row 1)
        self.question_text = Label(self.question_frame, text="",
                               justify=LEFT, width=40, bg=background_colour2, wrap=250)
        self.question_text.grid(row=1)

        # Close button (row 2)
        self.close_btn = Button(self.question_frame, text="Close",
                                  width=10, bg="deep sky blue", font=("Calibri", 10, "bold"),
                                  command=partial(self.close_question, partner))
        self.close_btn.grid(row=2, pady=10)

    def close_question(self, partner):
        # Put instructions button back to normal..
        partner.start_button.config(state=NORMAL)
        # close the window
        self.question_box.destroy()


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Aotearoa Place Quiz")
    quiz = MaoriQuiz()
    root.mainloop()

