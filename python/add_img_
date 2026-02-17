# Make sure you upload image in your current Repl
# Import all the necessary libraries
# PIL (Python Imaging Library) provides image editing capabilities to the python interpreter

from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title('image')
root.geometry('400x400')

upload = Image.open(r"C:\Users\SWEETY JOSHI\OneDrive\Desktop\codingal new folder\python\img.jpg")

image1 = ImageTk.PhotoImage(upload)

label = Label(root, image=image1, height=350, width=300)
label.place(x=50, y=0)

label2 = Label(root, text="This is how you add image in Tkinter Window")
label2.place(x=40, y=360)


root.mainloop()
