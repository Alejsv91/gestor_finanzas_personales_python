from ..utils.validators import checkInstance

class TransactionCategory:
    _name: str
    _enabled: bool
    
    def __init__(self, name: str, enabled: bool):
        self.name = name
        self.enabled = enabled
    
    #property
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
        
        

        
    