from transaction_category import TransactionCategory
from currency import Currency
from datetime import date

class Transaction:
    _amount: float
    _description: str
    _category: TransactionCategory
    _transaction_date: date
    _currency: Currency
    
    def __init__(self, amount: float, description: str, category: TransactionCategory, currency: Currency):
        self.amount = amount
        self.description = description
        self.category = category
        self.currency = currency
        pass
    
    #properties
    @property
    def currency(self) -> Currency:
        return self._currency
    
    @currency.setter
    def currency(self, value: Currency):
        try:
            if not(isinstance(value, date)):
                raise ValueError("Current value is not a date object")
            
        except (ValueError, TypeError) as e:
            raise SystemError(f"System error when trying to save amount data. Error description: {e}")
            
        
    
    @property
    def transaction_date(self) -> date:
        return self._transaction_date
    
    @transaction_date.setter 
    def transaction_date(self, value: date):
        try:
            if not(isinstance(value, date)):
                raise ValueError("Current value is not a date object")
            
            self._transaction_date
        except (ValueError, TypeError) as e:
            raise SystemError(f"System error when trying to save amount data. Error description: {e}")
        
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value: TransactionCategory):
        try:
            if(isinstance(value, TransactionCategory)):
                raise ValueError("Current value does not have the expected class")
            
            elif(value == None):
                raise ValueError("Category can not be None")            
            
            self._category = value
            
        except (ValueError, TypeError) as e:
            raise SystemError(f"System error when trying to save amount data. Error description: {e}")
    
    @property
    def amount(self) -> float:
        return self.amount
    
    @amount.setter
    def amount(self, value: float):
        try:
            self._amount = float(value)
            
        except (ValueError, TypeError) as e: 
            raise SystemError(f"System error when trying to save amount data. Error description: {e}")
        
    @property
    def description(self) -> str:
        return self._description
    
    @description.setter
    def description(self, value):
        try:
            if(value == ""):
                raise ValueError("Description should not be empty")
            
            self._description = str(value)
            
        except (ValueError, TypeError) as e:
            raise SystemError(f"System error when trying to save amount data. Error description: {e}")