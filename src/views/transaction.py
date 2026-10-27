import FreeSimpleGUI as sg
from ..models.transaction import Transaction
from ..models.enums import TransactionType, ExpenseKey 
from ..utils.csv_utils import save_transactions, read_transaction_category_data, read_currency_data, read_transactions_data
from ..models.transaction_category import TransactionCategory
from datetime import date

class TransactionView:
    _transaction_categories: list[TransactionCategory] = []
    _id_name_list: list[str] = []
    
    def __init__(self, transaction_type: TransactionType):
        self.transaction_type = transaction_type
        
        if self.transaction_type == TransactionType.EXPENSE:
            self.title = "Expense Manager"
            self.button_text = "Save Expense"
        else:
            self.title = "Income Manager"
            self.button_text = "Save Income"
            
        self.transaction_categories = read_transaction_category_data()
        self.create_dropdown_data()
        self.create_layout()
        
    @property
    def transaction_categories(self) -> list[TransactionCategory]:
        return self._transaction_categories
    
    @transaction_categories.setter
    def transaction_categories(self, value: list[TransactionCategory]):
        self._transaction_categories = value
        
    def create_layout(self):
        self.layout = [
            [sg.Text("Description: "), sg.Input("Description", key=ExpenseKey.DESCRIPTION)],
            [sg.Text("Amount: "), sg.Input("Amount", key=ExpenseKey.AMOUNT)],
            [[sg.Text("Category: "), sg.DropDown(self._id_name_list, key=ExpenseKey.CATEGORY)]],
            [sg.Button(self.button_text, key=ExpenseKey.SAVE)],
        ]
    
    def create_dropdown_data(self):
        self._id_name_list = [f"{c.id} - {c.name}" for c in self._transaction_categories]
        
    def show(self):
        self.window = sg.Window(self.title, self.layout, font="Courier 12")
        while True:
            event, values = self.window.read()
            
            match event:
                case sg.WIN_CLOSED:
                    break
                
                case ExpenseKey.SAVE:
                    if self.save_transaction(values):
                        label = "Expense" if self.transaction_type == TransactionType.EXPENSE else "Income"
                        sg.popup(f"{label} saved!")
                        self.window.close()
                        break
                
                case _:
                    print("Unhandled event")
                    
    def get_category_id(self, value: str) -> int:
        return value.split(" - ")[0]
    
    def get_currency_code(self) -> str:
        currencies = read_currency_data()
        base = next(filter(lambda c: c.is_base is True, currencies), None)
        return base.code
    
    def save_transaction(self, values) -> bool:
        transactions: list[Transaction] = read_transactions_data()
        id = max(t.id for t in transactions) + 1 if len(transactions) > 0 else 0
        
        if values[ExpenseKey.CATEGORY] == "":
            sg.popup_error("You should select a category")
            return False
        
        if values[ExpenseKey.DESCRIPTION].strip() == "":
            sg.popup_error("You should add a description")
            return False
        
        try:
            amount_value = abs(float(values[ExpenseKey.AMOUNT]))
            if amount_value == 0:
                sg.popup_error("Amount should be greater than 0")
                return False
        except:
            sg.popup_error("Amount should be a valid number")
            return False
        
        if self.transaction_type == TransactionType.EXPENSE:
            amount_value = -amount_value  
        else:
            amount_value = amount_value   
        
        transaction_category_id = self.get_category_id(values[ExpenseKey.CATEGORY])
        currency_code = self.get_currency_code()
        
        new_transaction: Transaction = Transaction(
            id=id, 
            amount=amount_value, 
            description=str(values[ExpenseKey.DESCRIPTION]),
            transaction_category_id=int(transaction_category_id), 
            transaction_date=date.today(),
            currency_code=str(currency_code),
            transaction_type=self.transaction_type 
        )
        
        save_transactions(new_transaction)
        return True
