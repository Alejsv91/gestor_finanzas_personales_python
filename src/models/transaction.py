from .transaction_category import TransactionCategory
from .enums import TransactionType
from .currency import Currency
from datetime import date
from ..utils.validators import checkInstance

class Transaction:
    _amount: float
    _description: str
    _category: TransactionCategory
    _transaction_date: date
    _currency: Currency
    _type: TransactionType
    
    def __init__(self, amount: float, description: str, category: TransactionCategory, currency: Currency, type: TransactionType):
        self.amount = amount
        self.description = description
        self.category = category
        self.currency = currency
        self.type = type
        pass
    
    #properties
    @property
    def type(self) -> TransactionType:
        return self._type
    
    @type.setter
    def type(self, value):
        checkInstance(value, TransactionType, "This value must be an instance of TransactionType")
        self._type = value
        
    @property
    def currency(self) -> Currency:
        return self._currency
    
    @currency.setter
    def currency(self, value: Currency):
        checkInstance(value, Currency, "This value must be an instance of Currency")
        self._currency = ValueError
            
    @property
    def transaction_date(self) -> date:
        return self._transaction_date
    
    @transaction_date.setter 
    def transaction_date(self, value: date):
        checkInstance(value, date, "This value must be an instance of date")
        self._transaction_date = value
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value: TransactionCategory):
        checkInstance(value, TransactionCategory, "This value must be an instance of TransactionCategory")
        self._category = value
    
    @property
    def amount(self) -> float:
        return self.amount
    
    @amount.setter
    def amount(self, value: float):
        checkInstance(value, float, "This value must be an instance of float")
        self._amount = value
        
    @property
    def description(self) -> str:
        return self._description
    
    @description.setter
    def description(self, value: str):
        checkInstance(value, str, "This value must be an instace of str")
        self._description = value