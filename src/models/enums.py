from enum import Enum

class TransactionType(Enum):
    INCOME = "INCOME"
    EXPENSE = "EXPENSE"
    
class FileNames(str, Enum):
    CURRENCY = "data/currency.csv"
    TRANSACTIONS = "data/transactions.csv"
    TRANSACTION_CATEGORY = "data/transaction_category.csv"
    
class ExpenseKey(Enum):
    DESCRIPTION = "DESCRIPTION"
    AMOUNT = "AMOUNT"
    CATEGORY = "CATEGORY"
    SAVE = "SAVE"
    
class TransactionTableKey(Enum):
    ADD_CATEGORY = "ADD_CATEGORY"
    ADD_EXPENSE = "ADD_EXPENSE"
    TABLE = "TABLE"
    ADD_INCOME = "ADD_INCOME"
    