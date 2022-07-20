import tkinter as tk
from forex_python.converter import CurrencyRates, CurrencyCodes

class CurrencyConverter:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Currency Converter")
        self.root.geometry("800x800")
        self.root.resizable(True, True)
        self.root.configure(background="white")
        self.root.protocol("WM_DELETE_WINDOW", self.close_window)
        
        self.button = tk.Button(self.root, text="Convert", font="Arial 12", bg="white", command=self.convert)
        self.button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        
        # create invert button
        self.invert_button = tk.Button(self.root, text="Invert", font="Arial 12", bg="white", command=self.invert)
        self.invert_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        
        
        pass
 
