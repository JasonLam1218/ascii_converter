import pytest
from unittest.mock import MagicMock, patch
from src.ascii_converter import AsciiConverter

@pytest.fixture
def mock_image_processor():
    mock = MagicMock()
    mock.load_image.return_value = MagicMock(name="mock_image")
    mock.convert_to_grayscale.return_value = MagicMock(name="mock_grayscale_image")
    mock.resize_image.return_value = MagicMock(name="mock_resized_image")
    # Simulate a 2x2 image with brightness values
    mock.get_pixel_brightness.return_value = [[10, 20], [30, 40]]
    return mock

@pytest.fixture
def mock_character_mapper():
    mock = MagicMock()
    # Define specific mappings for the dummy brightness values
    def map_side_effect(brightness):
        return {
            10: 'a',
            20: 'b',
            30: 'c',
            40: 'd',
        }.get(brightness, '?')
    mock.map_brightness_to_char.side_effect = map_side_effect
    return mock

@pytest.fixture
def ascii_converter(mock_image_processor, mock_character_mapper):
    # Patch ImageProcessor and CharacterMapper during AsciiConverter initialization
    with (
        patch('src.ascii_converter.ImageProcessor', return_value=mock_image_processor),
        patch('src.ascii_converter.CharacterMapper', return_value=mock_character_mapper)
    ):
        return AsciiConverter()

def test_convert_image_to_ascii(ascii_converter, mock_image_processor, mock_character_mapper):
    image_path = "test_image.jpg"
    output_width = 50
    
    # Call the method under test
    ascii_art = ascii_converter.convert_image_to_ascii(image_path, output_width)
    
    # Assertions to ensure correct flow and output
    mock_image_processor.load_image.assert_called_with(image_path)
    mock_image_processor.convert_to_grayscale.assert_called_with(mock_image_processor.load_image.return_value)
    mock_image_processor.resize_image.assert_called_with(mock_image_processor.convert_to_grayscale.return_value, output_width)
    mock_image_processor.get_pixel_brightness.assert_called_with(mock_image_processor.resize_image.return_value)
    
    # Ensure character mapping was called for each pixel
    expected_calls = [
        (10,), (20,),
        (30,), (40,)
    ]
    assert mock_character_mapper.map_brightness_to_char.call_args_list == [((b,),) for b in [10, 20, 30, 40]]
    
    # Assert the final ASCII art output
    assert ascii_art == "ab\ncd"
