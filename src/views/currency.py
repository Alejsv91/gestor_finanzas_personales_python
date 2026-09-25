import FreeSimpleGUI as sg
from ..models.currency import Currency
from ..utils.validators import checkInstance


class CurrencyView:
    _default_currencies: list[Currency] = []
    
    def __init__(self):
        self.default_currencies = [
            Currency("Colon Costarricense", "CRC", "₡", True),
            Currency("Dolar United States Of America", "USD", "$", False)]
        
    @property
    def default_currencies(self) -> list[Currency]:
        return self._default_currencies
    
    @default_currencies.setter
    def default_currencies(self, value: list[Currency]):
        checkInstance(value, list[Currency], "Values must be a instance of Currency")
        self._default_currencies = value
        
    def create_layout():
        # currency_options = Quede aqui
        layout =  [
            [sg.Text("Welcome to Keep Track App!")],
            [sg.Text("Select the base currency:")]
        ]
        
        
        
        