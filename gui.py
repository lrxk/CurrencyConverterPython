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
    def invert(self) -> None:
        self.from_currency = self.from_currency_entry.get()
        self.to_currency = self.to_currency_entry.get()
        self.from_currency_entry.delete(0, tk.END)
        self.from_currency_entry.insert(0, self.to_currency)
        self.to_currency_entry.delete(0, tk.END)
        self.to_currency_entry.insert(0, self.from_currency)
        pass
    def close_window(self) -> None:
        self.root.destroy()
        pass
    def convert(self) -> None:
        try:
            self.amount = float(self.amount_entry.get())
            self.from_currency = self.from_currency_entry.get()
            self.to_currency = self.to_currency_entry.get()
            self.result = self.amount * float(CurrencyRates().get_rate(self.from_currency, self.to_currency))
            # get to_currency symbol
            self.to_currency_symbol = CurrencyCodes().get_symbol(self.to_currency)
            self.result_label.configure(text=str(self.result) + " " + str(self.to_currency_symbol))
        except ValueError:
            self.result_label.configure(text="Invalid input")
        pass

