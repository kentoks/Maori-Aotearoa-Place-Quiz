"""Blank function to use enter questions.json
"""

# Prevents invalid blank input
def not_blank(question, error_msg, num_ok):
    error = error_msg
    valid = False

    while not valid:
        number = False  # Initial assumption - name contains no digits
        response = input(question)

        if not num_ok:  # set to False
            for letter in response:  # Check for digits in recipe name
                if letter.isdigit():  # Tests for True - by default
                    number = True  # Sets true if any digit found

        if not response or number is True:
            # generate error for blank name or digits
            print(error)

        else:  # no error found
            return response  # return bypasses the need to set 'valid' to True.
