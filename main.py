from src.views.transaction_table import TransactionTable
from src.models.transaction_category import TransactionCategory
from src.models.currency import Currency
from src.models.transaction import Transaction
from src.models.enums import *
from src.utils.csv_utils import file_exist
from src.views.currency import CurrencyView
from src.views.transaction_category_table import TransactionCategoryView
import FreeSimpleGUI as sg


def main():
    # Creating harcoded info
    # tc_comida = TransactionCategory("Comida", True)
    colon = Currency("Colon Costarricense", "CRC", "₡", True)
    # first_transaction = Transaction(10000.0, "Compras en Walmart", tc_comida, colon, TransactionType.EXPENSE)
    
    #Setup
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
        
    # Instantiates the table using the hardcoded default values
    view = TransactionTable()
    view.show()

if __name__ == "__main__":
    main()
