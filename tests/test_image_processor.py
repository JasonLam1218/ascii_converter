import pytest
from unittest.mock import MagicMock, patch
from src.image_processor import ImageProcessor
from PIL import Image
import os

# Mock the Image.open and Image.convert methods for testing
@pytest.fixture
def mock_image():
    mock = MagicMock(spec=Image.Image)
    mock.size = (100, 100)
    mock.convert.return_value = mock
    mock.resize.return_value = mock # Ensure resize returns the same mock object
    mock.getdata.return_value = [i for i in range(100 * 100)] # dummy pixel data
    return mock

@pytest.fixture
def image_processor():
    return ImageProcessor()

def test_load_image_success(image_processor, mock_image):
    with (
        patch('os.path.exists', return_value=True),
        patch('PIL.Image.open', return_value=mock_image)
    ):
        image = image_processor.load_image("dummy_path.jpg")
        assert image is mock_image

def test_load_image_file_not_found(image_processor):
    with patch('os.path.exists', return_value=False):
        with pytest.raises(FileNotFoundError):
            image_processor.load_image("non_existent_path.jpg")

def test_convert_to_grayscale(image_processor, mock_image):
    grayscale_image = image_processor.convert_to_grayscale(mock_image)
    mock_image.convert.assert_called_with("L")
    assert grayscale_image is mock_image

def test_resize_image(image_processor, mock_image):
    new_width = 50
    mock_image.size = (100, 100) # Reset size for this test
    resized_image = image_processor.resize_image(mock_image, new_width)
    expected_height = int((new_width / 100) * 100 * 0.55)
    mock_image.resize.assert_called_with((new_width, expected_height))
    assert resized_image is mock_image

def test_get_pixel_brightness(image_processor, mock_image):
    mock_image.size = (2, 2)
    mock_image.getdata.return_value = [10, 20, 30, 40]
    brightness_matrix = image_processor.get_pixel_brightness(mock_image)
    assert brightness_matrix == [[10, 20], [30, 40]]
