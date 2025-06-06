class CharacterMapper:
    def __init__(self, char_set: str):
        """
        Initializes the CharacterMapper with a set of ASCII characters.
        The characters are ordered from darkest (e.g., space) to lightest (e.g., '@', '#').
        """
        self.char_set = char_set

    def map_brightness_to_char(self, brightness: int) -> str:
        """
        Maps a brightness value (0-255) to an ASCII character from the char_set.
        Lower brightness (darker pixel) maps to denser characters.
        Higher brightness (lighter pixel) maps to sparser characters.
        """
        # Invert brightness: 0 (black) becomes 255, 255 (white) becomes 0.
        # This makes darker pixels correspond to higher indices in the char_set (denser characters).
        inverted_brightness = 255 - brightness
        
        # Scale the inverted brightness to an index within the character set range.
        # The last character in char_set corresponds to max inverted brightness.
        index = int((inverted_brightness / 255) * (len(self.char_set) - 1))
        
        return self.char_set[index]
