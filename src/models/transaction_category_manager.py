from ..models.transaction_category import TransactionCategory

class TransactionCategoryManager:
    
    @staticmethod
    def create_transaction_category(categories: list[TransactionCategory], new_category_name: str) -> TransactionCategory:
        if len(categories) > 0:
            new_id = max(category.id for category in categories) + 1
        else:
            new_id = 0
        
        return TransactionCategory(
            new_id,
            new_category_name,
            True                    
        )
    
    @staticmethod
    def validate_inputs(category_name: str) -> {"error", "message"}:
        status = {"error": False,
                  "message": ""}
        
        if(category_name.strip() == ""):
            status["error"] = True
            status["message"] = "Category name should not be empty"

        return status
        
    @staticmethod
    def create_table_values(categories: list[TransactionCategory]):
        return [ [obj.id, obj.name, obj.enabled]
                for obj in categories ]
        
    @staticmethod
    def check_and_new_transaction(new_category: TransactionCategory, categories: list[TransactionCategory]) -> list[TransactionCategory]:
        if isinstance(new_category, list):
            for item in new_category:
                if any(category.name.lower() == item.name.lower() for category in categories):
                    raise ValueError(f"The transaction '{item.name}' already exist")
                
                categories.append(item)
                
        elif isinstance(new_category, TransactionCategory):    
            exist = any(
                category.name.lower() == new_category.name.lower()
                for category in categories
            )
        
            if exist:
                print(f"The transaction '{new_category.name}' exist")
                raise ValueError(f"The transaction '{new_category.name}' already exists")
                    
            categories.append(new_category)
        
        return categories
        