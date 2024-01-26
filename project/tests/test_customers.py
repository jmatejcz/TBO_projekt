import pytest
from project.customers.models import Customer

def test_valid_customer():
    assert Customer(name="John Doe", city="Sample City", age=30, pesel="1234567890", street="Sample Street", appNo="123")

def test_invalid_name():
    with pytest.raises(ValueError):
        Customer(name="", city="Sample City", age=30, pesel="1234567890", street="Sample Street", appNo="123")

def test_invalid_city():
    with pytest.raises(ValueError):
        Customer(name="John Doe", city="", age=30, pesel="1234567890", street="Sample Street", appNo="123")

def test_invalid_age():
    with pytest.raises(ValueError):
        Customer(name="John Doe", city="Sample City", age=-1, pesel="1234567890", street="Sample Street", appNo="123")

def test_invalid_pesel():
    with pytest.raises(ValueError):
        Customer(name="John Doe", city="Sample City", age=30, pesel="invalid", street="Sample Street", appNo="123")

def test_invalid_street():
    with pytest.raises(ValueError):
        Customer(name="John Doe", city="Sample City", age=30, pesel="1234567890", street="", appNo="123")

def test_invalid_appNo():
    with pytest.raises(ValueError):
        Customer(name="John Doe", city="Sample City", age=30, pesel="1234567890", street="Sample Street", appNo="")

def test_pesel_too_short():
    with pytest.raises(ValueError):
        Customer(name="John Doe", city="Sample City", age=30, pesel="123", street="Sample Street", appNo="123")

def test_pesel_too_long():
    with pytest.raises(ValueError):
        Customer(name="John Doe", city="Sample City", age=30, pesel="123456789012345", street="Sample Street", appNo="123")

def test_name_invalid_type():
    with pytest.raises(TypeError):
        Customer(name=123, city="Sample City", age=30, pesel="1234567890", street="Sample Street", appNo="123")

def test_city_invalid_type():
    with pytest.raises(TypeError):
        Customer(name="John Doe", city=123, age=30, pesel="1234567890", street="Sample Street", appNo="123")

def test_age_invalid_type():
    with pytest.raises(TypeError):
        Customer(name="John Doe", city="Sample City", age="thirty", pesel="1234567890", street="Sample Street", appNo="123")

def test_pesel_invalid_type():
    with pytest.raises(TypeError):
        Customer(name="John Doe", city="Sample City", age=30, pesel=1234567890, street="Sample Street", appNo="123")

def test_street_invalid_type():
    with pytest.raises(TypeError):
        Customer(name="John Doe", city="Sample City", age=30, pesel="1234567890", street=123, appNo="123")

def test_appNo_invalid_type():
    with pytest.raises(TypeError):
        Customer(name="John Doe", city="Sample City", age=30, pesel="1234567890", street="Sample Street", appNo=123)