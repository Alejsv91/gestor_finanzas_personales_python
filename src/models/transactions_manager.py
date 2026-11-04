from ..models.enums import TransactionType
from ..utils.csv_utils import read_currency_data, save_transactions_to_csv, read_transactions_data
from ..models.transaction import Transaction
from datetime import date

class TransactionManager:

    @staticmethod
    def validate_inputs(category: str, description: str, amount: str) -> {"error", "message"}:
        status = {
            "error": False,
            "message": ""
        }
        
        if category.strip() == "":
            status["error"] = True
            status["message"] ="Please select one category"
            return status
        
        if description.strip() == "":
            status["error"] = True
            status["message"] = "Please add a description"
            return status
        
        if amount.strip() == "":
            status["error"] = True
            status["message"] = "Please add an amount"
            return status
        
        try:
            amount_value = abs(float(amount.strip()))
            if amount_value == 0:
                status["error"] = True
                status["message"] = "Amount should be greater than 0"
                return status
            
        except:
            status["error"] = True
            status["message"] = "Amount should be a valid number"
            return status
        
        return status
            
    @staticmethod
    def get_new_transaction_id():
        transactions: list[Transaction] = read_transactions_data()
        return max(t.id for t in transactions) + 1 if len(transactions) > 0 else 0
    
    @staticmethod
    def save_transaction( transaction_type: TransactionType, category: str,
                         description: str, amount: str) -> bool:
        
        amount_value = float(amount.strip())
        
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