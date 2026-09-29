from enum import Enum

class TransactionType(Enum):
    INCOME = "INCOME"
    EXPENSE = "EXPENSE"
    
class FileNames(str, Enum):
    CURRENCY = "data/currency.csv",
    TRANSACTIONS = "data/transactions.csv"
    TRANSACTION_CATEGORY = "data/transaction_category.csv"