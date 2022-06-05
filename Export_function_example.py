
class Export:
    def __init__(self, partner, r_results):
        # print(calc_history)   # For testing purposes
        background = "#a9ef99"  # Pale Green

        # disable export button
        partner.export_button.config(state=DISABLED)

        # sets up child window (i.e. export box)
        self.export_box = Toplevel()

        # If users press cross at the top, closes export window and 'releases'
        # export button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export,
                                                             r_results))

        # set up GUI frame
        self.export_frame = Frame(self.export_box, width=300, bg=background)
        self.export_frame.grid()

        # set up export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export Instructions",
                                 font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)

        # Export text (label, row 1)
        self.export_text = Label(self.export_frame,
                                 text="Enter a filename in the box below and "
                                      "press the Save button to save your "
                                      "calculation history to a text file.",
                                 justify=LEFT, width=40, bg=background,
                                 wrap=250)
        self.export_text.grid()

        # Warning text (label, row 2)
        self.export_text = Label(self.export_frame,
                                 text="If the filename you enter below "
                                      "already exists, it's contents will be "
                                      "replaced with your calculation history."
                                 , justify=LEFT, bg="#ffafaf",  # Pink
                                 fg="maroon", font="Arial 10 italic",
                                 padx=10, pady=10,
                                 wrap=225)
        self.export_text.grid(row=2, pady=10)

        # Filename entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error Message labels (row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon",
                                      bg=background)
        self.save_error_label.grid(row=4)

        # Save / Cancel Frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and Cancel Buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  command=partial(lambda: self.save_history
                                  (partner, r_results)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    command=partial(self.close_export,
                                                    partner))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner, calc_history):
        # Regular expression to check file name. Can be Upper or Lower case letters
        valid_char = "[A-Za-z0-9_]"  # Numbers or underscores
        has_error = "no"

        filename = self.filename_entry.get()
        # print(filename)
        for letter in filename:
            if re.match(valid_char, letter):
                continue  # If the letter is valid, goes back and checks the next

            elif letter == " ":  # Otherwise, find problem
                problem = "(no spaces allowed)"
            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":  # Describe problem
            # Display error message
            self.save_error_label.config(text="Invalid filename - {}".
                                         format(problem))
            # Change entry box background to pink
            self.filename_entry.config(bg="#ffafaf")
            print()
        else:
            # If there are no errors, generate text file and then close
            # dialogue. Add .txt suffix!

            filename = filename + ".txt"

            # Create file to hold data
            f = open(filename, "w+")

            # add new line at end of each item
            for item in calc_history:
                f.write(item + "/n")

            # close file
            f.close()

            # close dialogue
            self.close_export(partner)

    def close_export(self, partner, r_results):
        # Put export button back to normal
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()
