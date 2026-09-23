class Currency:
    name: str
    code: str
    symbol: str
    is_base: bool
    
    def __init__(self, name: str, code: str, symbol: str, is_base: bool):
        self.name = name
        self.code = code
        self.symbol = symbol
        self.is_base = is_base   