from tkinter import *

root = Tk()
root.title("Maori Aotearoa Place Quiz")

# Creating the file location to add image
maori_image = PhotoImage(file="christchurch.png")

# Placing the image into the label
maori_image_label = Label(root, image=maori_image)
maori_image_label.pack()
