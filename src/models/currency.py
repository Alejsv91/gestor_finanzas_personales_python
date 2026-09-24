from ..utils.validators import checkInstance

class Currency:
    _name: str
    _code: str
    _symbol: str
    _is_base: bool
    
    def __init__(self, name: str, code: str, symbol: str, is_base: bool):
        self.name = name
        self.code = code
        self.symbol = symbol
        self.is_base = is_base  
        
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        checkInstance(value, str, "This value should be a string")
        self._name = value
    
    @property
    def code(self) -> str: 
        return self._code
    
    @code.setter
    def code(self, value: str):
        checkInstance(value, str, "This value should be a string")
        self._code = value
    
    @property
    def symbol(self) -> str:
        return self._symbol
    
    @symbol.setter
    def symbol(self, value: str):
        checkInstance(value, str, "This value should be a string")
        self._symbol = value
        
    @property
    def is_base(self) -> bool:
        return self._is_base
    
    @symbol.setter
    def is_base(self, value: bool):
        checkInstance(value, bool, "This value should be a bool")
        self._is_base = value