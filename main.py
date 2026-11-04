from src.views.transaction_table import TransactionTable
from src.models.enums import FileNames
from src.utils.csv_utils import file_exist
from src.views.currency import CurrencyView
from src.views.transaction_category_table import TransactionCategoryView
from pathlib import Path
import FreeSimpleGUI as sg


def main():
    
    #Setup
    data_path = Path(FileNames.FOLDER_DATA)
    data_path.mkdir(parents=True, exist_ok=True)
    
    if not file_exist(FileNames.CURRENCY):
        print("We need to setup the currency")
        sg.popup("We need to setup the currency")
        view = CurrencyView()
        view.show()
        
    if not file_exist(FileNames.TRANSACTION_CATEGORY):
        print("We need to setup transaction categories")
        sg.popup("We need to setup transaction categories")
        view = TransactionCategoryView(False)
        view.show()
        
    view = TransactionTable()
    view.show()

if __name__ == "__main__":
    main()
