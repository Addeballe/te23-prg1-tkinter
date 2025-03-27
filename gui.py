from tkinter import *
from random import randint

root = Tk()
w = Label(root, text='Program that fucking kills itself!')
w.pack()

kill_button = Button(root, text='Kill Button', width=30, height=5, command=root.destroy)
kill_button.pack()



root.mainloop()