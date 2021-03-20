# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 23:13:36 2021

@author: Konstantinos
"""

import random
import tkinter as tk


class Window(tk.Frame):
    
    def __init__(self, parent):
        tk.Frame.__init__(self, parent) 
        self.parent = parent
        self.password = tk.StringVar()
        self.password.set('Here shows the password')
        self.length = tk.IntVar() 
        self.length.set(12) 
        self.symbols = tk.IntVar() 
        self.symbols.set(1) 
        self.capLetters = tk.IntVar()
        self.capLetters.set(1) 
        self.smaLetters = tk.IntVar()
        self.smaLetters.set(1)
        self.numbers = tk.IntVar()
        self.numbers.set(1)
        self.excsim = tk.IntVar()
        self.excsim.set(0)
        self.excamg = tk.IntVar()
        self.excamg.set(0)
        self.initUI()
        

    def CreatePassword(self):
        aps = []
        
        if self.symbols.get():
            aps.extend([i for i in range(33,48)])
            aps.extend([i for i in range(58,65)])
            aps.extend([i for i in range(91,97)])
            aps.extend([i for i in range(123,127)])
            
        if self.numbers.get():
            aps.extend([i for i in range(48,58)])
            
        if self.capLetters.get():
            aps.extend([i for i in range(65,91)])
            
        if self.smaLetters.get():
            aps.extend([i for i in range(97,123)])
            
        if self.excsim.get():
            aps.extend([i for i in [105, 73, 108, 76, 49, 111, 48, 79]])
            
        if self.excamg.get():
            aps.extend([123, 124, 91, 93, 40, 41, 47, 92, 96, 126, 39, 34, 44, 59, 58, 46, 60, 62])
        
        random.shuffle(aps)
        fc = random.sample(aps, self.length.get())
            
        fs = ''
        for i in fc:
            fs += chr(i)
        
        self.password.set(fs)    


        
    def initUI(self):
        '''
        Initialize the main window.

        Returns
        -------
        None.

        '''
        # Window title
        self.parent.title("Gradients Calculator")

        # Input frame
        inFrame = tk.Frame(self.parent)
        inFrame.grid(row=0, column=0)
        
        # Length box label
        lenLabel = tk.Label(inFrame, text='Define the length of the password: ')
        lenLabel.grid(row=0, column=0)
        
        # Length box     
        lenBox = tk.Entry(inFrame, textvariable=self.length, text=str(self.length), width=6)
        lenBox.grid(row=0, column=1)
        
        # Include symbols
        symBox = tk.Checkbutton(inFrame, text='Do you want to include symbols?', variable=self.symbols, onvalue=1, offvalue=0)
        symBox.grid(row=1, column=0)
        
        # Include capital letters
        capBox = tk.Checkbutton(inFrame, text='Do you want to include capital leters?', variable=self.capLetters, onvalue=1, offvalue=0)
        capBox.grid(row=2, column=0)
        
        # Include small letters
        capBox = tk.Checkbutton(inFrame, text='Do you want to include small letters?', variable=self.smaLetters, onvalue=1, offvalue=0)
        capBox.grid(row=3, column=0)
        
        # Include numbers
        numBox = tk.Checkbutton(inFrame, text='Do you want to include numbers?', variable=self.numbers, onvalue=1, offvalue=0)
        numBox.grid(row=4, column=0)
        
        # Exclude similar characters
        excSimBox = tk.Checkbutton(inFrame, text='Do you want to exclude similar characters?', variable=self.excsim, onvalue=1, offvalue=0)
        excSimBox.grid(row=5, column=0)
        
        # Exclude ambiguous characters
        excAmbBox = tk.Checkbutton(inFrame, text='Do you want to include capital leters?', variable=self.excamg, onvalue=1, offvalue=0)
        excAmbBox.grid(row=6, column=0)
              
        # Output frame
        outFrame = tk.Frame(self.parent)
        outFrame.grid(row=1, column=0)

        passBox = tk.Entry(outFrame, text=self.password, width=60, state='normal')
        passBox.grid(row=9, column=0)

        button = tk.Button(outFrame, text='Generate', command=self.CreatePassword)
        button.grid(row=7, column=0)


    


def main():

    root = tk.Tk()
    root.resizable(width=False, height=False)
    ex = Window(root)
    # root.geometry("460x200")
    root.geometry("485x240")
    root.mainloop()  


if __name__ == '__main__':
    main()

  