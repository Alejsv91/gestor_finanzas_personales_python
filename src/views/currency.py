import FreeSimpleGUI as sg
from ..models.currency import Currency
from ..utils.csv_utils import save_currencies
import sys


class CurrencyView:
    _default_currencies: list[Currency] = []
    
    def __init__(self):
        self.default_currencies = [
            Currency("Colon Costarricense", "CRC", "₡", True),
            Currency("Dolar United States Of America", "USD", "$", False)]
        self.window = self.create_layout()
        
    @property
    def default_currencies(self) -> list[Currency]:
        return self._default_currencies
    
    @default_currencies.setter
    def default_currencies(self, value: list[Currency]):
        self._default_currencies = value
        
    def show(self):
        window = self.create_layout()
        
        while True:
            event, values = window.read()
            
            if event == sg.WIN_CLOSED:
                sg.popup_ok("Closing app")
                sys.exit()
            
            if event == "Continue":
                self.set_base_currency(values)
                save_currencies(self.default_currencies)
                window.close()   
                break     
    
    def set_base_currency(self, base_currency_config: dict[str, bool]) -> list[Currency]:
        for currency in self.default_currencies:
            currency.is_base = base_currency_config[currency.code]
        
    def create_layout(self):
        currency_options = [
            Currency("Colon Costarricense", "CRC", "₡", True),
            Currency("Dolar United States Of America", "USD", "$", False)]
        
        title =  [
            [sg.Text("Select the base currency:")]
        ]
        
        currencies = self.create_radiobutton(currency_options)
        buttons = [
            [sg.Button("Continue")],
            ]    
        
        layout = title + currencies + buttons
        
        return sg.Window("Welcome to  Kepp Track App!", layout)
    
    def create_radiobutton(self, currency_options: list[Currency]):
        rb = []
        
        for curr in currency_options:
            rb.append([sg.Radio(curr.name, "Currency", default=True, key=curr.code)])
            
        return rb