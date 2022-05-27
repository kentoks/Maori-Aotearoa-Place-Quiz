from tkinter import *
from functools import partial  # To prevent unwanted windows


class MaoriQuiz:
    def __init__(self):

        # Formatting variables...
        background_color = "deep sky blue"

        # Converter Main Screen GUI...
        self.quiz_frame = Frame(width=300, height=300,
                                     bg=background_color, pady=10)
        self.quiz_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.quiz_heading_label = Label(self.quiz_frame,
                                          text="Maori Aotearoa Place Quiz",
                                          font=("Calibri", 16, "bold"),
                                          bg="lightgoldenrod",
                                          padx=10, pady=10)
        self.quiz_heading_label.grid(row=0)

        # instructions Button (row 1)
        self.instructions_button = Button(self.quiz_frame, text="Instructions", font=(
            "Calibri", "14"), padx=10, pady=10, command=self.instructions)
        self.instructions_button.grid(row=1)

    def instructions(self):
        print("You asked for Instructions")
        get_instructions = Instructions(self)
        get_instructions.instructions_text.configure(text="Instruction text goes here")


class Instructions:
    def __init__(self, partner):

        background = "lightgoldenrod"

        # disable instructions button
        partner.instructions_button.config(state=DISABLED)

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
                                    font=("Calibri", 10, "bold"), bg=background)
        self.how_heading.grid(row=0)

        # instructions text (label, row 1)
        self.instructions_text = Label(self.instructions_frame, text="",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.instructions_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.instructions_frame, text="Dismiss",
                                  width=10, bg="lightgoldenrod", font=("Calibri", 10, "bold"),
                                  command=partial(self.close_instructions, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_instructions(self, partner):
        # Put instructions button back to normal..
        partner.instructions_button.config(state=NORMAL)
        self.instructions_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Aotearoa Place Quiz")
    something = MaoriQuiz()
    root.mainloop()
