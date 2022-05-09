""" Kent Nago
"""

# Import Tools
from tkinter import * # For GUI Display
from functools import partial # To Prevent Unwanted Windows
import csv # For External States File and Saves File


# Menu GUI Class
class Menu:
    # Initialize Function
    def __init__(self):
        # Define Formatting Variables
        bg_colour = "deep sky blue"

        # Main Frame
        self.frm_m = Frame(width=700, height=300, bg=bg_colour)
        self.frm_m.grid()

        # Heading (Row 0)
        self.lbl_m_heading = Label(self.frm_m,
                                   text="Maori Aotearoa Place Quiz",
                                   font=("Arial", "16", "bold"),
                                   bg=bg_colour,
                                   padx=10, pady=5)
        self.lbl_m_heading.grid(row=0)

        # Button Frame (Row 1)
        self.frm_m_buttons = Frame(self.frm_m, width=100, height=100, bg=bg_colour)
        self.frm_m_buttons.grid(row=1)

        # So that Width and Height is Measured in Pixels, Create 1x1 Image
        pixel_image = PhotoImage(width=1, height=1)

        # Play Game Button (Row 1 / Row 0)
        self.btn_m_game = Button(self.frm_m_buttons,
                                 text="Play",
                                 width=15, height=2,
                                 padx=1, pady=1,
                                 command=self.fnc_get_g)
        self.btn_m_game.grid(row=0)

    def fnc_get_g(self):
        g = Game(self)


# Game GUI Class
class Game:
    # Initialize Function
    def __init__(self, menu):
        # Define Formatting Variables
        bg_colour = "orange"

        # Disable Button in Menu
        menu.btn_m_game.configure(state=DISABLED)

        # Create Window
        self.box_g = Toplevel()
        self.box_g.protocol('WM_DELETE_WINDOW', partial(self.fnc_g_close, menu))

        # Main Frame
        self.frm_g = Frame(self.box_g, width=100, height=100, bg=bg_colour)
        self.frm_g.grid()

        # Heading (Row 0)
        self.lbl_g_heading = Label(self.frm_g,
                                   text="Game",
                                   font=("Arial", "16", "bold"),
                                   bg=bg_colour,
                                   padx=10, pady=5)
        self.lbl_g_heading.grid(row=0)


        # Footer Frame (Row 2)
        self.frm_g_footer = Frame(self.frm_g, width=100, height=20, bg=bg_colour)
        self.frm_g_footer.grid(row=2)

        # So that Width and Height is Measured in Pixels, Create 1x1 Image
        pixel_image = PhotoImage(width=1, height=1)

        # Close Button (Row 2 / Row 0)
        self.btn_g_close = Button(self.frm_g_footer,
                                 text="Close",
                                 width=10, height=2,
                                 padx=1, pady=1,
                                 command=partial(self.fnc_g_close, menu))
        self.btn_g_close.grid(row=0)

    def fnc_g_close(self, menu):
        # Re-enable Help Button
        menu.btn_m_game.configure(state=NORMAL)
        # Close Window
        self.box_g.destroy()


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maori Aotearoa Place Quiz")
    main_window = Menu()
    root.mainloop()
