import FreeSimpleGUI as sg
import sys
from ..models.transaction import Transaction
from ..models.enums import TransactionType, TransactionTableKey
from ..views.transaction_category_table import TransactionCategoryView
from .transaction import TransactionView
from ..utils.csv_utils import read_transactions_data

class TransactionTable:
    _headings: list[str]
    _transactions: list[Transaction]
    
    def __init__(self):
        self.transactions = read_transactions_data()
        self.headings = ["id", "amount", "description", "transaction_category_id", 
                         "transaction_date", "currency_code", "transaction_type"]
        self.layout = [[sg.Button("Add category", key=TransactionTableKey.ADD_CATEGORY), 
                        sg.Button("Add Expense", key=TransactionTableKey.ADD_EXPENSE),
                        sg.Button("Add Income", key=TransactionTableKey.ADD_INCOME)],
                       [self.create_table()]]
        
    def show(self):
        self.window = sg.Window("Transactions table", self.layout, font="Courier 12")
        while True:
            event, values = self.window.read()
            
            match event:
                case sg.WIN_CLOSED:
                    sg.popup_ok("Closing app")
                    sys.exit()
                    break
                
                case TransactionTableKey.ADD_CATEGORY:
                    view = TransactionCategoryView(True)
                    view.show()
                
                case TransactionTableKey.ADD_EXPENSE:
                    self.save_transaction(TransactionType.EXPENSE)
                
                case TransactionTableKey.ADD_INCOME:
                    self.save_transaction(TransactionType.INCOME)
                    
                case _:
                    print("Unhandle event")
    
    def save_transaction(self, transaction_type: TransactionType):
        view = TransactionView(transaction_type)
        view.show()
        
        self.transactions = read_transactions_data()
        self.window[TransactionTableKey.TABLE].update(values=self.create_table_values())
                
        
    
    def create_table_values(self):
        if len(self.transactions) > 0:
            return [
                [t.id, t.amount, t.description, t.transaction_category_id, t.transaction_date, 
                t.currency_code, t.transaction_type.value]
                for t in self.transactions]        
        else:
            return []
            
    
    def create_table(self):
        return sg.Table(values=self.create_table_values(),
                        headings=self._headings,
                        key=TransactionTableKey.TABLE,
                        auto_size_columns=True,
                        expand_x=True,
                        expand_y=True
                        )
    
    @property
    def headings(self) -> list[str]:
        return self._headings
    
    @headings.setter
    def headings(self, value: list[str]):
        self._headings = []
        try:
            if not isinstance(value, list):
                ValueError("Value should not be None or empty")
            
            self._headings = value
            
        except (ValueError, TypeError) as e:
            raise SystemError(f"System error when trying to save amount data. Error description: {e}")
    
    @property
    def transactions(self) -> list[Transaction]:
        return self._transactions
    
    @transactions.setter
    def transactions(self, value: list[Transaction]):
        if not isinstance(value, list):
            sg.popup_error("transactions must be a instance of list[Transaction]")
            return
        
        self._transactions = value
        