import FreeSimpleGUI as sg
from ..models.transaction import Transaction
from ..utils.validators import checkInstance

class TransactionTable:
    _headings: list[str]
    
    def __init__(self, transactions: list[Transaction]):
        self.headings = transactions
        sg.theme('Dark Brown 1')
        header =  self.create_header()
        required_columns = len(self.headings)
        input_rows = [[sg.Input(size=(15,1), pad=(0,0)) for col in range(required_columns)] for row in range(10)]
        layout = header + input_rows
        window = sg.Window('Table Simulation', layout, font='Courier 12')
        event, values = window.read()
    
    @property
    def headings(self) -> list[str]:
        return self._headings
    
    @headings.setter
    def headings(self, value: list[Transaction]):
        self._headings = []
        try:
            if not value:
                ValueError("Value should not be None or empty")
            
            fr = value[0]
            for key in vars(fr).keys():
                self._headings.append(key.replace("_","").upper())
            
                     
        except (ValueError, TypeError) as e:
            raise SystemError(f"System error when trying to save amount data. Error description: {e}")
    
    def create_header(self) -> list[str]:
        return [[sg.Text('')] + [sg.Text(h, size=(14,1)) for h in self.headings]]
            
