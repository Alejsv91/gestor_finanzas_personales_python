from src.views.transaction_table import TransactionTable
from src.models.transaction_category import TransactionCategory
from src.models.currency import Currency
from src.models.transaction import Transaction
from src.models.enums import TransactionType

def main():
    # Creating harcoded info
    tc_comida = TransactionCategory("Comida", True)
    colon = Currency("Colon Costarricense", "CRC", "₡", True)
    first_transaction = Transaction(10000.0, "Compras en Walmart", tc_comida, colon, TransactionType.EXPENSE)
    
    # Instantiates the table using the hardcoded default values
    view = TransactionTable([first_transaction])
    view.show()

if __name__ == "__main__":
    main()
