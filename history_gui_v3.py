# will be adding new sub window to allow exporting to occur...
# will be adding items on the empty list for testings...

# will add string on list to be used for next version...


from tkinter import *
from functools import partial # to prevent unwanted windows
# functools prevent multiple instances from occuring, such as having multiple 'history' tabs
# now not importing json


# for now creating simple maori quiz interface (does not display question)
class MaoriQuiz:
    def __init__(self):

        # formatting variables...
        background_color = "deep sky blue"

        # initialise the list to hold the calculation history
        # simple test list to show the result exportation...
        self.all_answers = ['your results are 60%, no of wrong = 4, no of correct = 6',
                            'your results are 30%, no of wrong = 7, no of correct = 3',
                            'your results are 90%, no of wrong = 1, no of correct = 9']


        # converter main screen GUI...
        self.quiz_frame = Frame(width=300, height=300, bg=background_color,
                                     pady=10) # allows history button sizes at bottom to change
        # can use height=300, width=30,
        # but can be deleted, so the text can fit in the box
        self.quiz_frame.grid()

        # temperature conversion heading
        self.quiz_heading_label = Label(self.quiz_frame,
                                          text="Maori Aotearoa Place Quiz",
                                          font=("Calibri",18,"bold"),
                                          bg=background_color,
                                          padx=10, pady=10)

        self.quiz_heading_label.grid(row=0)

        # history button (row 1)
        self.ans_history_button = Button(self.quiz_frame, text="Answer History",
                                  font=("Calibri", 12,),
                                  padx=10, pady=5, command=self.history)
        self.ans_history_button.grid(row=1)


    def history(self):
        print("You have asked for History?")
        get_history = history(self)
        get_history.ans_history_text.configure(text="History text will appear here") # what does it do?


class history:
    def __init__(self, partner): # what is partner?
        background = "pale green" # hex code for pale green
        # a9ef99 does not work

        # disable 'history' button
        partner.ans_history_button.config(state=DISABLED) # what does state mean?

        # sets up child window (ie: history box)
        self.history_box = Toplevel()

        # if users press cross at top, it will close 'history' and and 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history,
                                                           partner))

        # sets up GUI frame
        self.history_frame = Frame(self.history_box, width=300, bg=background)
        self.history_frame.grid()

        # sets up history heading (row 0) (1st row)
        self.how_heading = Label(self.history_frame, text="Calculation History",
                                 font=("Calibri", 12, "bold"), bg=background)
        self.how_heading.grid(row=0)


        self.ans_history_text = Label(self.history_frame,
                                  text="Here are your most recent calculations"
                                       ". Please use the export button to "
                                       "create a text file of all your "
                                       "calculations for this session",
                                  justify=LEFT, width=40, bg=background,
                                  wrap=250, font=("Calibri", 10, "italic"), fg="maroon",
                                  pady=10, padx=10)
        self.ans_history_text.grid(row=1)


        # history output goes here... (row 2)

        # export / dismiss buttons frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # export button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font=("Calibri", 11, "bold"))
        self.export_button.grid(row=0, column=0)

        # dismiss button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     bg="orange", font=("Calibri", 11, "bold"),
                                     command=partial(self.close_history, partner))

        self.dismiss_button.grid(row=0, column=1)

    def close_history(self, partner):
        # put history button back to normal...
        partner.history_button.config(state=NORMAL) # returns the 'disabled' to 'normal' to make it reopenable
        self.history_box.destroy() # remember about destroy() which is just closing the box

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Aotearoa Place Quiz")
    something = MaoriQuiz()
    root.mainloop()
