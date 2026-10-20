import FreeSimpleGUI as sg
from ..models.transaction import Transaction
from ..utils.validators import checkInstance
from ..views.transaction_category_table import TransactionCategoryView

class TransactionTable:
    _headings: list[str]
    _transactions: list[Transaction]
    
    def __init__(self):
        # self.headings = transactions
        self.layout = [[sg.Button("Add category")]]
        
    def show(self):
        self.window = sg.Window("Transactions table", self.layout, font="Courier 12")
        while True:
            event, values = self.window.read()
            
            if event == sg.WIN_CLOSED:
                break
            
            if event == 'Add category':
                view = TransactionCategoryView(True)
                view.show()
    
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