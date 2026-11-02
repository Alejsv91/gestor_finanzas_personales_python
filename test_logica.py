import pytest
from src.models.transaction_category import TransactionCategory 
from datetime import date
from src.models.enums import TransactionType
from src.models.transaction import Transaction
from unittest.mock import MagicMock
from src.models.transactions_manager import TransactionManager

# =====================================================================
# TESTS PARA: validate_inputs
# =====================================================================

def test_validate_inputs_success(mocker):
    """Debe retornar el valor absoluto flotante si todos los datos son válidos."""
    mocker.patch('FreeSimpleGUI.popup_error')
    
    result = TransactionManager.validate_inputs("Food", "Groceries", "-150.50")
    assert result == 150.50

@pytest.mark.parametrize("category, description, amount, expected_msg", [
    ("", "Desc", "100", "Please select one category"),
    ("Food", "", "100", "Please add a description"),
    ("Food", "Desc", "", "Please add an amount"),
    ("Food", "Desc", "0", "Amount should be greater than 0"),
    ("Food", "Desc", "not_a_number", "Amount should be a valid number"),
])
def test_validate_inputs_failures(mocker, category, description, amount, expected_msg):
    """Debe mostrar el error correcto en el popup y retornar False ante inputs inválidos."""
    mock_popup = mocker.patch('FreeSimpleGUI.popup_error')
    
    result = TransactionManager.validate_inputs(category, description, amount)
    
    assert result is False
    mock_popup.assert_called_once_with(expected_msg)


# =====================================================================
# TESTS PARA: save_transaction
# =====================================================================

def test_save_transaction_invalid_inputs(mocker):
    """Debe retornar False inmediatamente si la validación falla sin abrir ventanas."""
    mocker.patch("src.models.transactions_manager.sg.popup_error") 
    
    result = TransactionManager.save_transaction(TransactionType.EXPENSE, "", "", "")
    
    assert result is False

    
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
    """Verifica que el validador lance un ValueError si el ID no es un entero."""
    with pytest.raises(ValueError):
        TransactionCategory(id="no_soy_un_int", name="Salud", enabled=True)

def test_name_setter_raises_error_on_invalid_type():
    """Verifica que el validador lance un ValueError si el nombre no es una cadena."""
    with pytest.raises(ValueError):
        TransactionCategory(id=2, name=12345, enabled=True)

def test_enabled_setter_raises_error_on_invalid_type():
    """Verifica que el validador lance un ValueError si el estado no es booleano."""
    with pytest.raises(ValueError):
        TransactionCategory(id=3, name="Educación", enabled="True_String")


# ==========================================
# ESCENARIOS POSITIVOS (Casos de éxito)
# ==========================================

def test_transaction_initialization_success():
    """Valida la creación exitosa con tipos correctos."""
    today = date.today()
    tx = Transaction(
        id=1,
        amount=1500.50,
        description="Pago de almuerzo",
        transaction_category_id=2,
        transaction_date=today,
        currency_code="CRC",
        transaction_type=TransactionType.EXPENSE
    )
    
    assert tx.id == 1
    assert tx.amount == 1500.50
    assert tx.description == "Pago de almuerzo"
    assert tx.transaction_category_id == 2
    assert tx.transaction_date == today
    assert tx.currency_code == "CRC"
    assert tx.transaction_type == TransactionType.EXPENSE

def test_transaction_type_setter_with_valid_strings():
    """Prueba que el setter maneje cadenas con formato largo como '.EXPENSE' o '.INCOME'."""
    today = date.today()
    tx = Transaction(1, 50.0, "Test", 1, today, "USD", TransactionType.EXPENSE)
    
    tx.transaction_type = "EXPENSE"
    assert tx.transaction_type == TransactionType.EXPENSE
    
    tx.transaction_type = "INCOME"
    assert tx.transaction_type == TransactionType.INCOME

def test_transaction_to_dict_conversion():
    """Verifica que to_dict exporte correctamente todos los campos."""
    today = date.today()
    tx = Transaction(10, 350.0, "Servicios", 4, today, "USD", TransactionType.EXPENSE)
    
    expected = {
        "id": 10,
        "amount": 350.0,
        "description": "Servicios",
        "transaction_category_id": 4,
        "transaction_date": today,
        "currency_code": "USD",
        "transaction_type": "EXPENSE"
    }
    
    print("---------------------")
    print(expected)
    print("---------------------")
    print(tx)
    
    
    assert tx.to_dict() == expected


# ==========================================
# ESCENARIOS NEGATIVOS (Validaciones y Erreores)
# ==========================================

def test_setters_raise_error_on_invalid_types():
    """Prueba que los setters disparen fallos al recibir datos erróneos."""
    today = date.today()
    tx = Transaction(1, 50.0, "Test", 1, today, "USD", TransactionType.EXPENSE)
    
    with pytest.raises(ValueError):
        tx.id = "no-es-un-int"
        
    with pytest.raises(ValueError):
        tx.amount = "no-es-un-float"
        
    with pytest.raises(ValueError):
        tx.description = 12345
        
    with pytest.raises(ValueError):
        tx.transaction_category_id = [1]
        
    with pytest.raises(ValueError):
        tx.transaction_date = "2026-10-27"
        
    with pytest.raises(ValueError):
        tx.currency_code = 506
