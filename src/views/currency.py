import FreeSimpleGUI as sg
from ..models.currency import Currency
from ..utils.validators import checkInstance


class CurrencyView:
    _default_currencies: list[Currency] = []
    
    def __init__(self):
        self.default_currencies = [
            Currency("Colon Costarricense", "CRC", "₡", True),
            Currency("Dolar United States Of America", "USD", "$", False)]
        
        window = self.create_layout()
        
        while True:
            event, values = window.read()
            
            if event == (sg.WIN_CLOSED, "Cancel"):
                break
            
            if event == "Continue":
                base_currency = values
                print(f"Selected currency: {base_currency}")
                # Save the first csv with currency info
                
        
    @property
    def default_currencies(self) -> list[Currency]:
        return self._default_currencies
    
    @default_currencies.setter
    def default_currencies(self, value: list[Currency]):
        self._default_currencies = value
        
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
                   [sg.Button("Cancel")]]    
        
        layout = title + currencies + buttons
        
        return sg.Window("Welcome to  Kepp Track App!", layout)
    
    def create_radiobutton(self, currency_options: list[Currency]):
        rb = []
        
        for curr in currency_options:
            rb.append([sg.Radio(curr.name, "Currency", default=True, key=curr.code)])
            
        return rb            
        
        
        
        
        