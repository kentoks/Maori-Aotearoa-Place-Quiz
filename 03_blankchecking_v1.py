""" 3rd component of the basic functionality of the blank checking function
This does not do anything but shows that the program successfully works.
Version 1

Created by Kent Nago
"""

def temp_convert(self, to):
    print(to)

    # adding bg color for entries that have errors
    error = "#ffafaf" # hex code for 'pale pink', when entry box is string or error, prints this color

    # retrieve amount entered into Entry field
    to_answer = self.to_convert_entry.get() # gets the user inputs from the entry box on the converter
    # Interface/GUI

    # check that amount is valid
    try:
        to_answer = float(to_answer)

    except ValueError:
        self.answer_label.configure(text="Enter a number!!!", fg="red") # Configure?
        self.to_answer_entry.configure(bg=error) # bg error color remember, 'pale pink'

