import FreeSimpleGUI as sg
from ..models.transaction_category import TransactionCategory
from ..utils.csv_utils import save_transaction_categories
from ..utils.csv_utils import read_transaction_category_data

class TransactionCategoryView:
    _headings: list[str] = ['ID', 'NAME', 'IS ENABLE']
    _categories: list[TransactionCategory] = []
    
    def __init__(self, load_transactions_category: bool):
        self._categories: list[TransactionCategory] = []
        
        if load_transactions_category:
            self.categories = read_transaction_category_data()
            self.table_values = [
                [obj.id, obj.name, obj.enabled]
                for obj in self.categories
            ]
        else:
            self.table_values = []
            
        self.layout = [
            [sg.Text("Category Name:"), 
             sg.Input("Add the category name", key="CATEGORY_NAME"), 
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
        if isinstance(value, list):
            for item in value:
                if any(category.name.lower() == item.name.lower() for category in self._categories):
                    raise ValueError(f"The transaction '{item.name}' already exist")
                
                self._categories.append(item)
                
        elif isinstance(value, TransactionCategory):    
            exist = any(
                category.name.lower() == value.name.lower()
                for category in self._categories
            )
        
            if exist:
                print(f"The transaction '{value.name}' exist")
                raise ValueError(f"The transaction '{value.name}' already exists")
                    
            self._categories.append(value)
                
    @property
    def headings(self):
        return self._headings
    
    def add_category(self, values):
        if len(self.categories) > 0:
            new_id = max(category.id for category in self._categories) + 1
        else:
            new_id = 0
        
        category = TransactionCategory(
            new_id,
            values["CATEGORY_NAME"],
            True                    
        )
        
        try:
            self.categories = category
        except ValueError as e:
            sg.popup_error(str(e), title="Error")
            return 
                
        table_data = [
            [c.id, c.name, c.enabled]
            for c in self.categories
        ]
                
        self.window["TABLE"].update(values=table_data)
        
    def create_table(self, values: list[TransactionCategory] | None):
        return sg.Table(
            values=values,
            headings=self.headings,
            key="TABLE",
            auto_size_columns=True,
            expand_x=True,
            expand_y=True
        )
