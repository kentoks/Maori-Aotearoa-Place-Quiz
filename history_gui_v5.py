"""This is the continuing progress of the History GUI
It is copied from 9th_component_v4
Fixing lists that have under 3 inputs
"""

from tkinter import *
from functools import partial # to prevent unwanted windows
# functools prevent multiple instances from occuring, such as having multiple 'history' tabs


class MaoriQuiz:
    def __init__(self):

        # formatting variables...
        background_color = "deep sky blue"

        # initialise the list to hold the calculation history
        # 4 test list now
        # simple test list
        self.all_calculations_list = ['0F is converted to -17.8C!', '1F is converted to -17.2C!',
                                 '2F is converted to -16.7C!', '3F is converted to -16.1C!']


        # converter main screen GUI...
        self.converter_frame = Frame(width=300, height=300, bg=background_color,
                                     pady=10) # allows history button sizes at bottom to change
        # can use height=300, width=30,
        # but can be deleted, so the text can fit in the box
        # remember what Frame is...
        self.converter_frame.grid()

        # temperature conversion heading
        self.temp_converter_label = Label(self.converter_frame,
                                          text="Maori Aotearoa Place Quiz",
                                          font=("Calibri", 18 ,"bold"),
                                          bg=background_color,
                                          padx=10, pady=10)

        self.temp_converter_label.grid(row=0)

        # history button (row 1)
        self.history_button = Button(self.converter_frame, text="History",
                                  font=("Calibri", 14,),
                                  padx=10, pady=5, command=lambda: self.history(self.all_calculations_list))
        # allows to open history button with lists of calculation list inputs
        # from 'command=self.history' to 'command=lambda'
        self.history_button.grid(row=1)


    def history(self, calculation_history):
        History(self, calculation_history)

class History:
    def __init__(self, partner, calculation_history): # what is partner?
        background = "pale green" # hex code for pale green
        # a9ef99 does not work

        # disable 'history' button
        partner.history_button.config(state=DISABLED) # what does state mean?

        # sets up child window (ie: history box)
        self.history_box = Toplevel() # what is toplevel()?

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


        self.history_text = Label(self.history_frame,
                                  text="Here are your most recent calculations"
                                       ". Please use the export button to "
                                       "create a text file of all your "
                                       "calculations for this session",
                                  justify=LEFT, width=40, bg=background,
                                  wrap=250, font=("Calibri", 10, "italic"), fg="maroon",
                                  pady=10, padx=10)
        self.history_text.grid(row=1)


        # history output goes here... (row 2)
        history_string = ""
        if len(calculation_history) >= 3:
            # The list must be greater or equal to zero
            # it cannot be less than the number, since it could not print calculation history
            for item in range (0,3):
                history_string += calculation_history[len(calculation_history)-item-1] +"\n"

        else:
            for item in calculation_history:
                history_string += calculation_history[len(calculation_history) -
                                                      calculation_history.index(item)-1] + "\n"
                self.history_text.config(text="Here is your calculation "
                                              "history: You can use this "
                                              "export button to save this data"
                                              " to a text file if desired.")

        # Label to display calculation history to enter
        self.calculation_label = Label(self.history_frame, text=history_string, bg=background,
                                       font=("Calibri", 12), justify=LEFT)
        self.calculation_label.grid(row=2)

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
