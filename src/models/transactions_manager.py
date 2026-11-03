from ..models.enums import TransactionType, FileNames
from ..utils.csv_utils import read_currency_data, save_transactions_to_csv, read_transactions_data
from ..models.transaction import Transaction
from datetime import date
import FreeSimpleGUI as sg

class TransactionManager:
    @staticmethod
    def validate_inputs(category: str, description: str, amount: str) -> bool | float:
        if category == "":
            sg.popup_error("Please select one category")
            return False
        if description == "":
            sg.popup_error("Please add a description")
            return False
        if amount == "":
            sg.popup_error("Please add an amount")
            return False
        try:
            amount_value = abs(float(amount))
            if amount_value == 0:
                sg.popup_error("Amount should be greater than 0")
                return False
        except:
            sg.popup_error("Amount should be a valid number")
            return False
        
        return amount_value
            
    @staticmethod
    def get_new_transaction_id():
        transactions: list[Transaction] = read_transactions_data()
        return max(t.id for t in transactions) + 1 if len(transactions) > 0 else 0
    
    @staticmethod
    def save_transaction( transaction_type: TransactionType, category: str,
                         description: str, amount: str) -> bool:
        
        if (amount_value := TransactionManager.validate_inputs(category, description,
                                                         amount)) is False: return False
        
        if transaction_type == TransactionType.EXPENSE:
            amount_value = -amount_value  
        else:
            amount_value = amount_value
        
        transaction_category_id = TransactionManager.get_category_id(category)
        currency_code = TransactionManager.get_currency_code()
        
        new_transaction: Transaction = Transaction(
            id=TransactionManager.get_new_transaction_id(), 
            amount=amount_value, 
            description=str(description),
            transaction_category_id=transaction_category_id, 
            transaction_date=date.today(),
            currency_code=str(currency_code),
            transaction_type=transaction_type
        )
        
        save_transactions_to_csv(new_transaction)
        return True
    
    @staticmethod
    def get_category_id( value: str) -> int:
        return int(value.split(" - ")[0])
        
    @staticmethod
    def get_currency_code() -> str:
        currencies = read_currency_data()
        base = next(filter(lambda c: c.is_base is True, currencies), None)
        return base.code