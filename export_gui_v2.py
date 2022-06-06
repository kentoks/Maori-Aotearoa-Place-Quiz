# Repurposed from 9th_component_v5

from tkinter import *
from functools import partial  # To prevent unwanted windows


class MaoriQuiz:
    def __init__(self):

        # Formatting variables...
        background_color = "deep sky blue"

        # Initialise list to hold result history
        self.all_answer_list = ['Results: 60%, number of incorrect answers = 4, '
                            'number of correct answers = 6']


        # Main Screen GUI...
        self.quiz_frame = Frame(width=300, height=300,
                                     bg=background_color, pady=10)
        self.quiz_frame.grid()

        # Quiz label Heading (row 0)
        self.quiz_heading_label = Label(self.quiz_frame,
                                          text="Maori Aotearoa Place Quiz",
                                          font=("Calibri", "16", "bold",),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.quiz_heading_label.grid(row=0)

        # history Button (row 1)
        self.history_button = Button(self.quiz_frame, text="Export",
                                     font=("Calibri", "14"), padx=10, pady=10,
                                     command=lambda: self.history(self.all_answer_list))
        self.history_button.grid(row=1)

        if len(self.all_answer_list) == 0:
            self.history_button.config(state=DISABLED)

    def history(self, answer_history):
        AnsHistory(self, answer_history)


class AnsHistory:
    def __init__(self, partner, answer_history):

        background = "lightgoldenrod"

        # disable history button
        partner.history_button.config(state=DISABLED)

        # Sets up child window (history box)
        self.history_box = Toplevel()

        # If users press cross at top, closes history and 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_history, partner))

        # Set up GUI Frame
        self.history_frame = Frame(self.history_box, width=300, bg=background)
        self.history_frame.grid()

        # Set up history heading (row 0)
        self.how_heading = Label(self.history_frame, text="\nResult history",
                                 font="Calibri 14 bold", bg=background)
        self.how_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame,
                                  text="Here are your results"
                                       ". Please use the export button to "
                                       "create a text file of the results for this session",
                                  justify=LEFT, width=40, bg=background,
                                  wrap=250, font="Calibri 10 italic", fg="maroon")
        self.history_text.grid(row=1)

        # History output goes here... (row 2)
        history_string = ""
        if len(answer_history) >= 1:
            for item in range(0, 1):
                history_string += answer_history[len(answer_history)-item-1]+"\n"
        else:
            for item in answer_history:
                history_string += answer_history[len(answer_history) -
                                               answer_history.index(item)-1]+"\n"
                self.history_text.config(text="Here is your result "
                                              "history. You can use this "
                                              "export button to save this data"
                                              " to a text file if desired.")

        # Label to display result history to user
        self.calc_label = Label(self.history_frame, text=history_string,
                                bg=background, font="Calibri 12", justify=LEFT)
        self.calc_label.grid(row=2)

        # Export / Dismiss buttons frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export Button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="Calibri 10 bold", command=self.export)
        self.export_button.grid(row=0, column=0)

        # Dismiss Button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     font="Calibri 10 bold",
                                     command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)

    def close_history(self, partner):
        # Put history button back to normal...
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

    def export(self):
        get_export = Export(self)


class Export:
    def __init__(self, partner):

        background = "lightgoldenrod" 

        # disable export button
        partner.export_button.config(state=DISABLED)

        # Sets up child window (export box)
        self.export_box = Toplevel()

        # If users press cross at top, closes export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW',
                                 partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, width=300, bg=background)
        self.export_frame.grid()

        # Set up export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export instructions",
                                 font="Calibri 10 bold", bg=background)
        self.how_heading.grid(row=0)

        # Export text (label, row 1)
        self.export_text = Label(self.export_frame,
                                 text="Enter a file name in the box below and "
                                      "press the save button to save your "
                                      "result history to a text file",
                                 justify=LEFT, width=40, bg=background, wrap=250)
        self.export_text.grid(row=1)

        # Warning text (label, row 1)
        # adding in Version 3

        # Filename entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20, font="Calibri 14 bold",
                                    justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Save / Cancel Frame (row 4)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=4, pady=10)

        # Save and cancel buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save")
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def close_export(self, partner):
        # Put export button back to normal...
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Aotearoa Place Quiz")
    something = MaoriQuiz()
    root.mainloop()
