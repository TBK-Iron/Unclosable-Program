from tkinter import ttk
from tkinter import *

def disable_event():
    pass

root = Tk()
canvas = Canvas(root, width = 1150, height = 667)
canvas.pack()
img = PhotoImage(file="img.png")
canvas.create_image(0,0, anchor = NW, image = img)
root.title("Unclosable program")
root.protocol("WM_DELETE_WINDOW", disable_event)
root.iconbitmap(default="pig.ico")

root.mainloop()