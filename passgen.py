# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 23:13:36 2021

@author: Konstantinos
"""

import random
import tkinter as tk

root = tk.Tk()
root.resizable(width=False, height=False)

# root.geometry("460x200")
root.geometry("485x240")


# Length box label
lenLabel = tk.Label(root, text='Define the length of the password: ')
lenLabel.grid(row=0, column=0)

# Length box
length = tk.IntVar()
length.set(12)
lenBox = tk.Entry(root, textvariable=length, text=str(length), width=6)
lenBox.grid(row=0, column=1)

# Include symbols
symbols = tk.IntVar()
symbols.set(1)
symBox = tk.Checkbutton(root, text='Do you want to include symbols?', variable=symbols, onvalue=1, offvalue=0)
symBox.grid(row=1, column=0)

# Include capital letters
capLetters = tk.IntVar()
capLetters.set(1)
capBox = tk.Checkbutton(root, text='Do you want to include capital leters?', variable=capLetters, onvalue=1, offvalue=0)
capBox.grid(row=2, column=0)

# Include small letters
smaLetters = tk.IntVar()
smaLetters.set(1)
capBox = tk.Checkbutton(root, text='Do you want to include small letters?', variable=smaLetters, onvalue=1, offvalue=0)
capBox.grid(row=3, column=0)

# Include numbers
numbers = tk.IntVar()
numbers.set(1)
numBox = tk.Checkbutton(root, text='Do you want to include numbers?', variable=numbers, onvalue=1, offvalue=0)
numBox.grid(row=4, column=0)

# Exclude similar characters
excsim = tk.IntVar()
excsim.set(0)
excSimBox = tk.Checkbutton(root, text='Do you want to exclude similar characters?', variable=excsim, onvalue=1, offvalue=0)
excSimBox.grid(row=5, column=0)

# Exclude ambiguous characters
excamg = tk.IntVar()
excamg.set(0)
excAmbBox = tk.Checkbutton(root, text='Do you want to include capital leters?', variable=excamg, onvalue=1, offvalue=0)
excAmbBox.grid(row=6, column=0)

password = tk.StringVar()
password.set('test')
passBox = tk.Entry(root, text=password, width=60, state='normal')
passBox.grid(row=9, column=0)

aps = []

if symbols.get():
    aps.extend([i for i in range(33,48)])
    aps.extend([i for i in range(58,65)])
    aps.extend([i for i in range(91,97)])
    aps.extend([i for i in range(123,127)])
    
if numbers.get():
    aps.extend([i for i in range(48,58)])
    
if capLetters.get():
    aps.extend([i for i in range(65,91)])
    
if smaLetters.get():
    aps.extend([i for i in range(97,123)])
    
if excsim.get():
    aps.extend([i for i in [105, 73, 108, 76, 49, 111, 48, 79]])
    
if excamg.get():
    aps.extend([123, 124, 91, 93, 40, 41, 47, 92, 96, 126, 39, 34, 44, 59, 58, 46, 60, 62])

random.shuffle(aps)
fc = random.sample(aps, length.get())
    
fs = ''
for i in fc:
    fs += chr(i)

password.set(fs)

button = tk.Button(root, text='Generate')
button.grid(row=7, column=0)

root.mainloop()   