from enum import Enum

class TransactionType(Enum):
    INCOME = "INCOME"
    EXPENSE = "EXPENSE"
    
class FileNames(str, Enum):
    CURRENCY = "data/currency.csv"