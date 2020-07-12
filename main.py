from tkinter import *
import pandas as pd
from IPython.display import display



def submit():
    data_frame = pd.read_csv('data.csv')
    row = pd.Series([name.get(), phoneno.get(), timein.get(), timeout.get()], index=data_frame.columns)
    data_frame = data_frame.append(row, ignore_index = True )
    display(data_frame)
    data_frame.to_csv('data.csv', index = False)

root = Tk()


myLabel = Label(root, text ="wowowo")

name_label = Label(root, text="Name: ")
name = Entry(root)
phoneno_label = Label(root, text='Phone Number')
phoneno = Entry(root)
timein_label = Label(root, text='What time did you enter?')
timein = Entry(root)
timeout_label = Label(root, text='What time did you leave?')
timeout = Entry(root)
submit_button = Button(root, text='submit', bg = "#90EE90", command=submit)

name_label.pack()
name.pack()
phoneno_label.pack()
phoneno.pack()
timein_label.pack()
timein.pack()
timeout_label.pack()
timeout.pack()
submit_button.pack()

root.mainloop()