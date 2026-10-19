import FreeSimpleGUI as sg
from ..models.transaction_category import TransactionCategory
from ..utils.csv_utils import save_transaction_categories

class TransactionCategoryView:
    _headings: list[str] = ['NAME', 'IS ENABLE']
    
    def __init__(self):
        self._categories: list[TransactionCategory] = []
        self.layout = [
            [sg.Text("Category Name:"), 
             sg.Input("Add the category name", key="CATEGORY_NAME"), 
             sg.Button("Add Category")],                  
            [self.create_table()],
            [sg.Button("Next")]
        ]  
        self.window = None

    def show(self):
        """Este método abre la ventana y controla el bucle de eventos de forma segura"""
        self.window = sg.Window("Transaction category table", self.layout, font="Courier 12")
        
        while True:
            event, values = self.window.read()
            
            if event == sg.WIN_CLOSED:
                break
            
            if event == "Add Category":
                self.add_category(values)
            
            elif event == "Nex":
                save_transaction_categories(self.categories)
                break
                
        self.window.close() 
                             
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
            [c.name, c.enabled]
            for c in self.categories
        ]
                
        self.window["TABLE"].update(values=table_data)
        
    def create_table(self):
        return sg.Table(
            values=[],
            headings=self.headings,
            key="TABLE",
            auto_size_columns=True,
            expand_x=True,
            expand_y=True
        )
