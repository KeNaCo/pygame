#!/bin/python3

from tkinter import *
from tkinter import ttk
from tkinter import font

def on_clic():
	print("Entry value is:", username.get())
	bText.set(username.get())

root = Tk()
root.geometry("160x90")

frame = ttk.Frame(root, padding=(3,3,12,12))
frame['borderwidth'] = 5
frame.grid(column=0, row=0)

myFont = font.Font(family='Helvetica', size=20, weight='bold')
label = ttk.Label(frame, text='Some text..', font=myFont)

"""
resultsContents = StringVar()
label['textvariable'] = resultsContents
resultsContents.set('Some text old...')
label.bind('<1>', lambda e: resultsContents.set('New text to display'))
"""
"""
image = PhotoImage(file='tux_samurai.gif')
label['image']= image

label.grid(column=0, row=0, sticky=(W, E), padx=5, pady=5)
"""
var = IntVar()
check = ttk.Checkbutton(frame, text='Check Button', variable=var, command=lambda: print("Somebody klick on checkbutton. Value is: ", var.get()))
check.grid(column=0, row=1)

username = StringVar()
name = ttk.Entry(frame, textvariable=username)
#name['show'] = "*"
name.grid(column=0,row=2, sticky=(W, E), padx=5, pady=5)

bText = StringVar()
bText.set("def")
button = ttk.Button(frame, textvariable=bText, command=on_clic)
button.grid(column=0, row=3)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)
root.mainloop()
