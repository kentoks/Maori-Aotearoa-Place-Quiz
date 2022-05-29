# test to disable button

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
