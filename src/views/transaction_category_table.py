import FreeSimpleGUI as sg
from ..models.transaction_category import TransactionCategory
from ..utils.csv_utils import save_transaction_categories
from ..utils.csv_utils import read_transaction_category_data
from ..models.enums import TransactionCategoryTableKey
from ..models.transaction_category_manager import TransactionCategoryManager

class TransactionCategoryView:
    _headings: list[str] = ['ID', 'NAME', 'IS ENABLE']
    _categories: list[TransactionCategory] = []
    
    def __init__(self, load_transactions_category: bool):
        self._categories: list[TransactionCategory] = []
        
        if load_transactions_category:
            self.categories = read_transaction_category_data()
            self.table_values = TransactionCategoryManager.create_table_values(self.categories)
        else:
            self.table_values = []
            
        self.layout = [
            [sg.Text("Category Name:"), 
             sg.Input( key=TransactionCategoryTableKey.CATEGORY_NAME), 
             sg.Button("Add Category")],                  
            [self.create_table(self.table_values)],
            [sg.Button("Save and Close")]
        ]  
        self.window = None

    def show(self):
        self.window = sg.Window("Transaction category table", self.layout, font="Courier 12")
        
        while True:
            event, values = self.window.read()
            
            if event == sg.WIN_CLOSED:
                if self.categories == []:
                    sg.popup_error("Warning: You are closing the category creation screen without adding any categories. You must add at least one category to save future transactions.")
                break
            
            if event == "Add Category":
                self.add_category(values)
            
            elif event == "Save and Close":
                if not(len(self.categories) > 0):
                    sg.popup_error("Please add at least one category")
                else:
                    save_transaction_categories(self.categories)
                    break
                
        self.window.close() 
                             
    @property
    def categories(self) -> list[TransactionCategory]:
        return self._categories
    
    @categories.setter
    def categories(self, value: TransactionCategory):
        self._categories = TransactionCategoryManager.check_and_new_transaction(value, self._categories)
                
    @property
    def headings(self):
        return self._headings
    
    def add_category(self, values):
        try: 
            new_category_name = values[TransactionCategoryTableKey.CATEGORY_NAME]
            
            validation_status = TransactionCategoryManager.validate_inputs(new_category_name)
            
            if(validation_status["error"]):
                sg.popup_error(validation_status["message"])
                return
            
            tc = TransactionCategoryManager.create_transaction_category(self.categories, new_category_name)
        
            self.categories = tc
            
            self.window["TABLE"].update(values=TransactionCategoryManager.create_table_values(self.categories))
            
        except ValueError as e:
            sg.popup_error(str(e), title="Error")
            return 
                        
    def create_table(self, values: list[TransactionCategory] | None):
        return sg.Table(
            values=values,
            headings=self.headings,
            key="TABLE",
            auto_size_columns=True,
            expand_x=True,
            expand_y=True
        )
