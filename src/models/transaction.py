from transaction_category import TransactionCategory
from currency import Currency
from datetime import date

class Transaction:
    _amount: float
    _description: str
    _category: TransactionCategory
    _date: date
    _currency: Currency
    
    def __init__(self, amount: float, description: str, category: TransactionCategory, currency: Currency):
        amount
        pass
    
    #properties
    @property
    def amount(self) -> float:
        return self.amount
    
    @amount.setter
    def amount(self, value: float):
        try:
            self._amount = float(value)
        except (ValueError, TypeError) as e: 
            raise ValueError(f"System error when trying to save amount data. Error description: {e}")
        
    @property
    def description(self) -> str:
        return self._description
    
    @description.setter
    def description(self, value):
        try:
            self._description = str(value)
        except (ValueError, TypeError) as e:
            raise ValueError(f"System error when trying to save amount data. Error description: {e}")
            
            
        
    
    