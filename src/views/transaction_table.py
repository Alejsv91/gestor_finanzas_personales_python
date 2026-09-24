import FreeSimpleGUI as sg
from ..models.transaction import Transaction
from ..utils.validators import checkInstance

class TransactionTable:
    _headings: list[str]
    
    def __init__(self, transactions: list[Transaction]):
        self.headings = transactions
        sg.theme('Dark Brown 1')

        header =  [[sg.Text('  ')] + [sg.Text(h, size=(14,1)) for h in self.headings]]

        input_rows = [[sg.Input(size=(15,1), pad=(0,0)) for col in range(4)] for row in range(10)]

        layout = header + input_rows

        window = sg.Window('Table Simulation', layout, font='Courier 12')
        event, values = window.read()
    
    @property
    def headings(self) -> list[str]:
        return self.headings
    
    @headings.setter
    def headings(self, value: list[Transaction]):
        try:
            if not value:
                ValueError("Value should not be None or empty")
            
            fr = value[0]
            self._headings = [key.capitalize() for key in vars(fr).keys()]
                     
        except (ValueError, TypeError) as e:
            raise SystemError(f"System error when trying to save amount data. Error description: {e}")
            
