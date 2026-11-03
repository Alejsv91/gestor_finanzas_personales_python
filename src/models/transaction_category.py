from ..utils.validators import check_instance

class TransactionCategory:
    _name: str
    _enabled: bool
    _id: int
    
    def __init__(self, id: int ,name: str, enabled: bool):
        self.name = name
        self.enabled = enabled
        self.id = id
    
    #properties
    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, value: int):
        check_instance(value, int, "Transaction id instance should be int")
        self._id = value        
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        check_instance(value, str, "The name of the transaction summary type is string")
        self._name = value
        
    @property
    def enabled(self) -> bool:
        return self._enabled
    
    @enabled.setter
    def enabled(self, value):
        check_instance(value, bool, "enabled value should be bool type")
        self._enabled = value
        
        
    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "enabled": self.enabled,
            "id" :self.id
        }
        
        

        
    