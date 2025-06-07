import pytest
from app import convert_to_uppercase

def test_convert_to_uppercase():
    assert convert_to_uppercase("hello") == "HELLO"
    assert convert_to_uppercase("world") == "WORLD"
    assert convert_to_uppercase("Python") == "PYTHON"
    assert convert_to_uppercase("123") == "123"
    assert convert_to_uppercase("") == ""
    assert convert_to_uppercase("Hello World") == "HELLO WORLD"
    assert convert_to_uppercase("TESTING 123!") == "TESTING 123!"
    assert convert_to_uppercase("already UPPERCASE") == "ALREADY UPPERCASE" 