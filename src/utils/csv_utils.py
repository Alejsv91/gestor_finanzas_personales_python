import csv
from pathlib import Path
from ..models.currency import Currency
from ..models.enums import FileNames
from ..models.transaction_category import TransactionCategory
from ..models.transaction import Transaction
from datetime import date, datetime
import FreeSimpleGUI as sg

def save_transactions(transaction: Transaction) -> None:
    transactions = read_transactions_data()
    transactions.append(transaction)
    try:
        with open(FileNames.TRANSACTIONS, "w", newline="", encoding="utf-8") as file:
            writeDataAsDict(file, ["id", "amount", "description",
                                   "transaction_category_id","transaction_date",
                                   "currency_code", "transaction_type"], 
                            transactions)
            
    except ValueError as e:
        sg.popup_error(str(e), title="System Error")

def save_transaction_categories(transaction_categories: list[TransactionCategory]) -> None:
    try: 
        with open(FileNames.TRANSACTION_CATEGORY, "w", newline="", encoding="utf-8") as file:
            writeDataAsDict(file, ["id","name", "enabled"], transaction_categories)
            
        sg.popup("Transaction Category data saved!")
        
    except ValueError as e:
        sg.popup_error(str(e), title="Error")

def save_currencies(currencies: list[Currency]) -> None:
    with open(FileNames.CURRENCY, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["name", "code", "symbol", "is_base"]
        ) 
        
        writer.writeheader()
        
        for currency in currencies:
            writer.writerow(currency.to_dict())
            
def writeDataAsDict(file, titleList: list[str], items: list[any]):
    writer = csv.DictWriter(
        file,
        fieldnames=titleList
    ) 
    
    writer.writeheader()
        
    for item in items:
        writer.writerow(item.to_dict())

def read_transactions_data() -> list[Transaction]:
    if not file_exist(FileNames.TRANSACTIONS):
        return []
    
    transactions: list[Transaction] = []
    with open(FileNames.TRANSACTIONS, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
                transactions.append(Transaction(id=int(row["id"]), 
                                                amount=float(row["amount"]), 
                                                description=row["description"],
                                                transaction_category_id=int(row["transaction_category_id"]),
                                                transaction_date=datetime.strptime(row["transaction_date"], '%Y-%m-%d').date(),
                                                currency_code=str(row["currency_code"]),
                                                transaction_type=row["transaction_type"]
                                                ))
        
        return transactions

def read_transaction_category_data() -> list[TransactionCategory]:
    if not file_exist(FileNames.TRANSACTION_CATEGORY):
        return []
    
    transaction_category: list[TransactionCategory] = []
    with open(FileNames.TRANSACTION_CATEGORY, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            transaction_category.append(
                TransactionCategory(id=int(row["id"]),
                                    name=str(row["name"]),
                                    enabled=row["enabled"] == "True"
            ))
            
    return transaction_category
    
            
def read_currency_data() -> list[Currency]:
    if not file_exist(FileNames.CURRENCY):
        return []
    
    currencies: list[Currency] = []
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
