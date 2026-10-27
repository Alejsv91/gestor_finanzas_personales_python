import pytest
from unittest.mock import patch
from src.models.transaction_category import TransactionCategory 
from datetime import date
from src.models.enums import TransactionType
from src.models.transaction import Transaction

# ==========================================
# ESCENARIOS POSITIVOS (Casos de éxito)
# ==========================================

def test_transaction_category_initialization_success():
    """Valida que una categoría se instancie correctamente con valores válidos."""
    category = TransactionCategory(id=1, name="Alimentación", enabled=True)
    
    assert category.id == 1
    assert category.name == "Alimentación"
    assert category.enabled is True

def test_transaction_category_to_dict_conversion():
    """Verifica el mapeo correcto de los atributos a un diccionario estructurado."""
    category = TransactionCategory(id=5, name="Transporte", enabled=False)
    expected_dict = {
        "id": 5,
        "name": "Transporte",
        "enabled": False
    }
    
    assert category.to_dict() == expected_dict

def test_setters_update_values_correctly():
    """Comprueba que las propiedades permitan modificar los valores internos con tipos válidos."""
    category = TransactionCategory(id=1, name="Inicial", enabled=True)
    
    category.id = 10
    category.name = "Modificado"
    category.enabled = False
    
    assert category.id == 10
    assert category.name == "Modificado"
    assert category.enabled is False


# ==========================================
# ESCENARIOS NEGATIVOS (Validaciones de Tipo)
# ==========================================

def test_id_setter_raises_error_on_invalid_type():
    """Verifica que el validador lance un TypeError si el ID no es un entero."""
    with pytest.raises(SystemError):
        TransactionCategory(id="no_soy_un_int", name="Salud", enabled=True)

def test_name_setter_raises_error_on_invalid_type():
    """Verifica que el validador lance un TypeError si el nombre no es una cadena."""
    with pytest.raises(SystemError):
        TransactionCategory(id=2, name=12345, enabled=True)

def test_enabled_setter_raises_error_on_invalid_type():
    """Verifica que el validador lance un TypeError si el estado no es booleano."""
    with pytest.raises(SystemError):
        TransactionCategory(id=3, name="Educación", enabled="True_String")


# ==========================================
# ESCENARIOS POSITIVOS (Casos de éxito)
# ==========================================

def test_transaction_initialization_success():
    """Valida la creación exitosa con tipos correctos."""
    hoy = date.today()
    tx = Transaction(
        id=1,
        amount=1500.50,
        description="Pago de almuerzo",
        transaction_category_id=2,
        transaction_date=hoy,
        currency_code="CRC",
        transaction_type=TransactionType.EXPENSE
    )
    
    assert tx.id == 1
    assert tx.amount == 1500.50
    assert tx.description == "Pago de almuerzo"
    assert tx.transaction_category_id == 2
    assert tx.transaction_date == hoy
    assert tx.currency_code == "CRC"
    assert tx.transaction_type == TransactionType.EXPENSE

def test_transaction_type_setter_with_valid_strings():
    """Prueba que el setter maneje cadenas con formato largo como '.EXPENSE' o '.INCOME'."""
    hoy = date.today()
    tx = Transaction(1, 50.0, "Test", 1, hoy, "USD", TransactionType.EXPENSE)
    
    tx.transaction_type = "transactionType.EXPENSE"
    assert tx.transaction_type == TransactionType.EXPENSE
    
    tx.transaction_type = "transactionType.INCOME"
    assert tx.transaction_type == TransactionType.INCOME

def test_transaction_to_dict_conversion():
    """Verifica que to_dict exporte correctamente todos los campos."""
    hoy = date.today()
    tx = Transaction(10, 350.0, "Servicios", 4, hoy, "USD", TransactionType.EXPENSE)
    
    expected = {
        "id": 10,
        "amount": 350.0,
        "description": "Servicios",
        "transaction_category_id": 4,
        "transaction_date": hoy,
        "currency_code": "USD",
        "transaction_type": TransactionType.EXPENSE
    }
    assert tx.to_dict() == expected


# ==========================================
# ESCENARIOS NEGATIVOS (Validaciones y Erreores)
# ==========================================

def test_setters_raise_error_on_invalid_types():
    """Prueba que los setters disparen fallos al recibir datos erróneos."""
    hoy = date.today()
    # Instanciamos un objeto base válido para mutar sus propiedades
    tx = Transaction(1, 50.0, "Test", 1, hoy, "USD", TransactionType.EXPENSE)
    
    # Cada una de estas asignaciones debería levantar un TypeError según tu validador
    with pytest.raises(SystemError):
        tx.id = "no-es-un-int"
        
    with pytest.raises(SystemError):
        tx.amount = "no-es-un-float"
        
    with pytest.raises(SystemError):
        tx.description = 12345
        
    with pytest.raises(SystemError):
        tx.transaction_category_id = [1]
        
    with pytest.raises(SystemError):
        tx.transaction_date = "2026-10-27"
        
    with pytest.raises(SystemError):
        tx.currency_code = 506