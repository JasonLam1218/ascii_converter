import os
from PIL import Image

class ImageProcessor:
    def load_image(self, image_path: str) -> Image.Image:
        """
        Loads an image from the specified path.
        Raises FileNotFoundError if the file does not exist.
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file not found: {image_path}")
        return Image.open(image_path)

    def convert_to_grayscale(self, image: Image.Image) -> Image.Image:
        """
        Converts a PIL Image object to grayscale.
        'L' mode in PIL represents a single-channel grayscale image (0-255).
        """
        return image.convert("L")

    def resize_image(self, image: Image.Image, new_width: int) -> Image.Image:
        """
        Resizes the image to a new width, maintaining the aspect ratio
        while also correcting for character aspect ratio.
        ASCII characters are taller than they are wide, so we adjust height by 0.55.
        """
        width, height = image.size
        # Calculate new height based on new_width, maintaining aspect ratio,
        # and adjusting for the typical aspect ratio of text characters
        new_height = int((new_width / width) * height * 0.55)
        return image.resize((new_width, new_height))

    def get_pixel_brightness(self, image: Image.Image) -> list[list[int]]:
        """
        Extracts the brightness (pixel intensity) values from a grayscale image.
        Returns a 2D list (matrix) where each element is an integer from 0-255.
        """
        pixels = list(image.getdata())  # Get all pixel values as a flat list
        width, height = image.size
        brightness_matrix = []
        for i in range(height):
            row = []
            for j in range(width):
                # Calculate the index for the current pixel in the flat list
                row.append(pixels[i * width + j])
            brightness_matrix.append(row)
        return brightness_matrix

    def test_tkinter(self):
        tkinter._test()
