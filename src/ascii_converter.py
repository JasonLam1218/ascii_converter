from src.image_processor import ImageProcessor
from src.character_mapper import CharacterMapper

class AsciiConverter:
    def __init__(self, char_set: str = " .:-=+*#%@"):
        """
        Initializes the AsciiConverter with an ImageProcessor and CharacterMapper.
        A default character set is provided, but can be customized.
        """
        self.image_processor = ImageProcessor()
        self.character_mapper = CharacterMapper(char_set)

    def convert_image_to_ascii(self, image_path: str, output_width: int = 100) -> str:
        """
        Main method to convert an image to ASCII art.
        """
        # Step 1: Load the image
        image = self.image_processor.load_image(image_path)
        
        # Step 2: Convert to grayscale
        grayscale_image = self.image_processor.convert_to_grayscale(image)
        
        # Step 3: Resize the image
        resized_image = self.image_processor.resize_image(grayscale_image, output_width)
        
        # Step 4: Get pixel brightness values
        brightness_matrix = self.image_processor.get_pixel_brightness(resized_image)

        ascii_art_lines = []
        # Step 5: Iterate through the brightness matrix and map each pixel to an ASCII character
        for row in brightness_matrix:
            ascii_row = "".join([self.character_mapper.map_brightness_to_char(pixel_brightness) for pixel_brightness in row])
            ascii_art_lines.append(ascii_row)
        
        # Step 6: Join the lines to form the complete ASCII art string
        return "\n".join(ascii_art_lines)
