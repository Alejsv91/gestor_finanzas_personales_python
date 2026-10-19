import FreeSimpleGUI as sg
from ..models.transaction_category import TransactionCategory

class TransactionCategoryView:
    _headings: list[str] = ['NAME', 'IS ENABLE']
    _categories: list[TransactionCategory] = []
    
    def __init__(self):
        self._categories = []
        # Add input fields
        layout = [[sg.Text("Category Name:"), 
                   sg.Input("Add the category name", key="CATEGORY_NAME"), 
                   sg.Button("Add Category")],                  
                  [self.create_table()]]  
                
        # creating window
        window = sg.Window("Transaction category table", layout, font="Courier 12")
        event, values = window.read()
        
        while True:
            event, values = window.read()
            
            if event == "Add Category":
                window = self.add_category(window, values)
                
                             
    @property
    def categories(self) -> list[TransactionCategory]:
        return self._categories
    
    @categories.setter
    def categories(self, value: TransactionCategory):
        exist = any(
            category.name.lower() == value.name.lower()
            for category in self._categories
        )
        
        if exist:
            print(f"The transaction '{value.name}' exist")
            raise ValueError(f"The transaction '{value.name}' exist")
                
        self._categories.append(value)
                
        
    @property
    def headings(self):
        return self._headings
    
    def add_category(self, window, values):
        category = TransactionCategory(
                    values["CATEGORY_NAME"],
                    True                    
                )
        
        try:
            self.categories = category
        except ValueError as e:
            sg.popup_error(str(e), title="Error")
                
        table_data = [
                    [c.name, c.enabled]
                    for c in self.categories
                ]
                
        window["TABLE"].update(values=table_data)
        return window
        
    def create_table(self):
        return sg.Table(values=[],
                 headings=self.headings,
                 key="TABLE",
                 auto_size_columns=True,
                 expand_x=True,
                 expand_y=True)
        # sg.theme('Dark Brown 1')
        # header = [[sg.Text('')] + [sg.Text(h, size=(14,1)) for h in self.headings]]
        # required_columns = len(self.headings)
        # input_rows = [[sg.Input(size=(15,1), pad=(0,0)) for col in range(required_columns)] for row in range(10)]
        
        # table_layout = [
        #     [sg.Text(h, size=(14, 1)) for h in self.headings]
        #     ] + input_rows
        
        # return [[sg.Column(table_layout,justification='center',expand_x=True)]]