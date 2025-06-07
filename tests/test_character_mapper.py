import pytest
from src.character_mapper import CharacterMapper

def test_character_mapper_initialization():
    mapper = CharacterMapper("abc")
    assert mapper.char_set == "abc"

def test_map_brightness_to_char():
    mapper = CharacterMapper(" .:-=+*#%@")
    
    # Test black (0 brightness) - should map to the darkest character (last in set)
    assert mapper.map_brightness_to_char(0) == "@"
    
    # Test white (255 brightness) - should map to the lightest character (first in set)
    assert mapper.map_brightness_to_char(255) == " "
    
    # Test mid-range brightness
    assert mapper.map_brightness_to_char(127) == "="
    
    # Test edge cases close to boundaries
    assert mapper.map_brightness_to_char(1) == "%"
    assert mapper.map_brightness_to_char(254) == " "
    
    # Test with a smaller character set
    small_mapper = CharacterMapper("XO")
    assert small_mapper.map_brightness_to_char(0) == "O"
    assert small_mapper.map_brightness_to_char(255) == "X"
    assert small_mapper.map_brightness_to_char(127) == "X"
