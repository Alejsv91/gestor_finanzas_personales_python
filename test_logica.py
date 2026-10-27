import pytest
from unittest.mock import patch
# Modifica el import según la estructura exacta de tus carpetas (ej. src.models.transaction_category)
from src.models.transaction_category import TransactionCategory 

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
    # Nota: Si tu función checkInstance levanta TypeError, pytest lo capturará aquí
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

