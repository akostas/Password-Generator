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
        # The final password
        self.password = tk.StringVar()
        self.password.set('Here shows the password')
        # The length of the password
        self.length = tk.IntVar() 
        self.length.set(12)
        # Include symbols, 1-yes, 2-no
        self.symbols = tk.IntVar() 
        self.symbols.set(1)
        # Include capital letters, 1-yes, 2-no
        self.capLetters = tk.IntVar()
        self.capLetters.set(1)
        # Include small letters, 1-yes, 2-no
        self.smaLetters = tk.IntVar()
        self.smaLetters.set(1)
        # Include numbers, 1-yes, 2-no
        self.numbers = tk.IntVar()
        self.numbers.set(1)
        # Exclude similar characters, 1-yes, 2-no
        self.excsim = tk.IntVar()
        self.excsim.set(0)
        # Exclude ambiguous characters, 1-yes, 2-no
        self.excamg = tk.IntVar()
        self.excamg.set(0)
        self.initUI()
        

    def symbolList(self):
        '''
        Function to create a list with all the possible symbols for the 
        password

        Returns
        -------
        aps : list
            list of symbols with the passworkd.

        '''
        aps = []
        # Import symbols
        if self.symbols.get():
            aps.extend([i for i in range(33,48)])
            aps.extend([i for i in range(58,65)])
            aps.extend([i for i in range(91,97)])
            aps.extend([i for i in range(123,127)])
        # Import numbers
        if self.numbers.get():
            aps.extend([i for i in range(48,58)])
        # Import capital letters
        if self.capLetters.get():
            aps.extend([i for i in range(65,91)])
        # Import small letters
        if self.smaLetters.get():
            aps.extend([i for i in range(97,123)])
        # Exclude similar characters
        if self.excsim.get():
            for i in [105, 73, 108, 76, 49, 111, 48, 79]:
                try:
                    aps.remove(i)
                except:
                    pass
        # Exclude ambiguous characters    
        if self.excamg.get():
            for i in [123, 124, 91, 93, 40, 41, 47, 92, 96, 126, 39, 34, 44, 59, 58, 46, 60, 62]:
                try:
                    aps.remove(i)
                except:
                    pass               
        return aps
        
    def getNrandom(self, aps):
        '''
        Function to create a list with N characters

        Parameters
        ----------
        aps : list
            list of symbols.

        Returns
        -------
        fc : list
            list of final symbols.

        '''
        # Randomize the list elements
        random.shuffle(aps)
        # Pick n random elements
        fc = [aps[random.randint(0, len(aps)-1)] for i in range(self.length.get()) ]
        return fc
    
    def convertASCII(self, fc):
        '''
        Function to convert ASCII numers to characters

        Parameters
        ----------
        fc : list
            list of ascii numbers.

        Returns
        -------
        fs : list
            list of characters.

        '''
        fs = ''
        for i in fc:
            fs += chr(i)      
        return fs

    def createPassword(self):
        '''
        Function to generate the password

        Returns
        -------
        None.

        '''
        # Get the symbols list
        aps = self.symbolList()
        # Get N symbols
        fc = self.getNrandom(aps)
        fs = self.convertASCII(fc)
        self.password.set(fs)    
        
    def copy_button(self):
        '''
        Function to copy password to clipboard

        Returns
        -------
        None.

        '''
        r = tk.Tk()
        r.withdraw()
        # r.clipboard_clear()
        r.clipboard_append(self.password.get())
        r.destroy()
        
    def initUI(self):
        '''
        Initialize the main window.

        Returns
        -------
        None.

        '''
        # Window title
        self.parent.title("Password Generator")

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
        excAmbBox = tk.Checkbutton(inFrame, text='Do you want to exclude ambiguous characters?', variable=self.excamg, onvalue=1, offvalue=0)
        excAmbBox.grid(row=6, column=0)
              
        # Output frame
        outFrame = tk.Frame(self.parent )
        outFrame.grid(row=1, column=0, columnspan=2)

        # Entry to print the password
        passBox = tk.Entry(outFrame, text=self.password, width=60, state='disabled')
        passBox.grid(row=1, column=0, columnspan=2)

        # Button to generate password
        genbut = tk.Button(outFrame, text='Generate', command=self.createPassword)
        genbut.grid(row=0, column=0)

        # Button to copy password
        copbut = tk.Button(outFrame, text='Copy', command=self.copy_button)
        copbut.grid(row=0, column=1)

    


def main():
    root = tk.Tk()
    root.resizable(width=False, height=False)
    Window(root)
    root.geometry("350x240")
    root.mainloop()  


if __name__ == '__main__':
    main()