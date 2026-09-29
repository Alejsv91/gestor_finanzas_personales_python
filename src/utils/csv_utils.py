import csv
from pathlib import Path
from ..models.currency import Currency
from ..models.enums import FileNames

def save_currencies(currencies: list[Currency]) -> None:
    with open(FileNames.CURRENCY, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["name", "code", "symbol", "is_base"]
        ) 
        
        writer.writeheader()
        
        for currency in currencies:
            writer.writerow(currency.to_dict())
            
def read_currency_data() -> list[Currency]:
    currencies = list[Currency]
    with open(FileNames.CURRENCY, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            currencies.append(
                Currency(
                    name=row["name"],
                    code=row["code"],
                    symbol=row["symbol"],
                    is_base=row["is_base"] == "True"
                )
            )
    
    return currencies
            
def file_exist(file_path: FileNames):
    fp = Path(file_path)
    
    return fp.exists()
        
    