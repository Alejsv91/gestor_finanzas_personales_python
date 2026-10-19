from ..utils.validators import checkInstance

class TransactionCategory:
    _name: str
    _enabled: bool
    _id: int
    
    def __init__(self, id: int ,name: str, enabled: bool):
        self.name = name
        self.enabled = enabled
        self.id = id
    
    #property
    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, value: int):
        self._id = value        
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        checkInstance(value, str, "The name of the transaction summary type is string")
        self._name = value
        
    @property
    def enabled(self) -> bool:
        return self._enabled
    
    @enabled.setter
    def enabled(self, value):
        checkInstance(value, bool, "enabled value should be bool type")
        self._enabled = value
        
        
    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "enabled": self.enabled,
            "id" :self.id
        }
        
        

        
    