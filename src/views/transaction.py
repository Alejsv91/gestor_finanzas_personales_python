import FreeSimpleGUI as sg
from ..models.enums import TransactionType, ExpenseKey 
from ..utils.csv_utils import  read_transaction_category_data
from ..models.transaction_category import TransactionCategory
from ..views.transaction_category_table import TransactionCategoryView
from ..models.transactions_manager import TransactionManager

class TransactionView:
    _transaction_categories: list[TransactionCategory] = []
    _id_name_list: list[str] = []
    _save_disabled: bool = True
    
    
    def __init__(self, transaction_type: TransactionType):
        self.transaction_type = transaction_type
        
        if self.transaction_type == TransactionType.EXPENSE:
            self.title = "Expense Manager"
            self.button_text = "Save Expense"
        else:
            self.title = "Income Manager"
            self.button_text = "Save Income"
            
        self.create_dropdown_data()
        self.create_layout()
        
    @property
    def transaction_categories(self) -> list[TransactionCategory]:
        return self._transaction_categories
    
    @transaction_categories.setter
    def transaction_categories(self, value: list[TransactionCategory]):
        self._transaction_categories = value
        
    def create_layout(self):
        dv = None
        if self._id_name_list:
            dv=self._id_name_list[0]
        
        self.layout = [
            [sg.Text("Description: "), sg.Input( key=ExpenseKey.DESCRIPTION)],
            [sg.Text("Amount: "), sg.Input(key=ExpenseKey.AMOUNT)],
            [[sg.Text("Category: "), sg.DropDown(values=self._id_name_list, key=ExpenseKey.CATEGORY,
                                                 default_value=dv), sg.Button("Add Category", key=ExpenseKey.ADD_CATEGORY)]],
            [sg.Button(self.button_text, key=ExpenseKey.SAVE, disabled=self._save_disabled), 
             sg.Text(text=self.warning_category_message(), key=ExpenseKey.NOT_CATEGORIES_MESSAGE, font=("Helvetica", 10, "bold"))],
        ]
    
    def warning_category_message(self):
        return "SAVE BUTTON DISABLED, please at least one category" if self._save_disabled == True else ""
    
    def create_dropdown_data(self):
        self.transaction_categories = read_transaction_category_data()
        if len(self.transaction_categories) > 0:
            self._id_name_list = [f"{c.id} - {c.name}" for c in self._transaction_categories]
            self._save_disabled = False
        else:
            self._id_name_list = []
            self._save_disabled = True
        
        
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
                
                case ExpenseKey.ADD_CATEGORY:
                    transaction_category_view = TransactionCategoryView(True)
                    transaction_category_view.show()
                    self.create_dropdown_data()
                    self.update_view()
                
                case _:
                    print("Unhandled event")
                    
    def update_view(self):
        self.window[ExpenseKey.CATEGORY].update(values=self._id_name_list, value=self._id_name_list[0])
        self.window[ExpenseKey.NOT_CATEGORIES_MESSAGE].update(self.warning_category_message())
        self.window[ExpenseKey.SAVE].update(disabled=self._save_disabled)
    
    def save_transaction(self, values) -> bool:
        status = TransactionManager.validate_inputs(values[ExpenseKey.CATEGORY], 
                                            values[ExpenseKey.DESCRIPTION], values[ExpenseKey.AMOUNT])
        if status["error"]:
            sg.popup_error(status["message"])
            return False
        else:
            return TransactionManager.save_transaction(self.transaction_type, values[ExpenseKey.CATEGORY], 
                                            values[ExpenseKey.DESCRIPTION], values[ExpenseKey.AMOUNT])
        
        
