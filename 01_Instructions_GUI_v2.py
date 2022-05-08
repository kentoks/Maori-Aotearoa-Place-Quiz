from tkinter import *
import random


class MaoriQuiz:
    def __init__(self):
        print("Hello World")

        # Formatting variables...
        background_color = "deep sky blue"

        # Converter Main Screen GUI...
        self.converter_frame = Frame(width=300, height=300, bg=background_color)
        self.converter_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.place_quiz_label = Label(text="Maori Aotearoa Place Quiz",
                                          font=("Calibri", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.place_quiz_label.grid(row=0)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Aotearoa Place Quiz")
    something = MaoriQuiz()
    root.mainloop()
