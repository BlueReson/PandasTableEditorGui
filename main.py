import tkinter as tk
import pandas as pd 
from pandastable import Table

class TableEditor:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Table Editor")
        
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        
        self.table = Table(self.frame, showstatusbar=True, showtoolbar=True)
        self.table.show()
        
        self.root.mainloop()
        
if __name__ == "__main__" :
    TableEditor()      