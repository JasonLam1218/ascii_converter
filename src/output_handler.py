class OutputHandler:
    def save_to_text_file(self, ascii_art: str, output_path: str):
        """
        Saves the given ASCII art string to a specified text file.
        """
        with open(output_path, "w") as f:
            f.write(ascii_art)
