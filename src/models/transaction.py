from .enums import TransactionType
from datetime import date
from ..utils.validators import checkInstance

class Transaction:
    _id: int
    _amount: float
    _description: str
    _transaction_category_id: int
    _transaction_date: date
    _currency_code: str
    _transaction_type: TransactionType
    
    def __init__(self,id: int, amount: float, description: str, transaction_category_id: int, transaction_date: date, currency_code: str, transaction_type: TransactionType):
        self.id = id
        self.amount = amount
        self.description = description
        self.transaction_category_id = transaction_category_id
        self.transaction_date = transaction_date
        self.currency_code = currency_code
        self.transaction_type = transaction_type
        
        
    #properties
    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, value: int):
        checkInstance(value, int, "Transaction id value should be an instance of int")
        self._id = value
    
    @property
    def transaction_type(self) -> TransactionType:
        return self._transaction_type
    
    @transaction_type.setter
    def transaction_type(self, value: TransactionType | str):
        if isinstance(value, str):
            if ".EXPENSE" in value:
                self._transaction_type = TransactionType.EXPENSE
            elif ".INCOME" in value:
                self._transaction_type = TransactionType.INCOME
            else:
                raise ValueError("The string value should be EXPENSE or INCOME")
            return
            
        checkInstance(value, TransactionType, "Transaction_type should be an instance of TransactionType")
        self._transaction_type = value
        
    @property
    def currency_code(self) -> str:
        return self._currency_code
    
    @currency_code.setter
    def currency_code(self, value: str):
        checkInstance(value, str, "This value must be an instance of int")
        self._currency_code = value
            
    @property
    def transaction_date(self) -> date:
        return self._transaction_date
    
    @transaction_date.setter 
    def transaction_date(self, value: date):
        checkInstance(value, date, "This value must be an instance of date")
        self._transaction_date = value
    
    @property
    def transaction_category_id(self) -> int:
        return self._transaction_category_id
    
    @transaction_category_id.setter
    def transaction_category_id(self, value: int):
        checkInstance(value, int, "This value must be an instance of int")
        self._transaction_category_id = value
    
    @property
    def amount(self) -> float:
        return self._amount
    
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
        
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "amount": self.amount,
            "description": self.description,
            "transaction_category_id" : self.transaction_category_id,
            "transaction_date": self.transaction_date,
            "currency_code": self.currency_code,
            "transaction_type": self.transaction_type
        }