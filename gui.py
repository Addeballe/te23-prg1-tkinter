from tkinter import *
from random import randint

root = Tk()
root.title('Program that nicely kills itself')
w = Label(root, text='Program that *nicely* kills itself!')
w.pack()

kill_button = Button(root, text='Kill Button', width=30, height=5, command=root.destroy)
kill_button.pack()

root.mainloop()