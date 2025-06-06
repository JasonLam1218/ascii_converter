from src.ascii_converter import AsciiConverter
from src.output_handler import OutputHandler
import argparse

def main():
    # Step 1: Set up argument parsing
    parser = argparse.ArgumentParser(description="Convert an image to ASCII art.")
    parser.add_argument("input_image", help="Path to the input image file.")
    parser.add_argument("-o", "--output_file", help="Optional: Path to save the ASCII art to a text file.", default=None)
    parser.add_argument("-w", "--width", type=int, default=100, help="Output width of the ASCII art (default: 100).")

    args = parser.parse_args() # Parse arguments from the command line

    # Step 2: Initialize converter and output handler
    converter = AsciiConverter()
    output_handler = OutputHandler()

    try:
        # Step 3: Perform the image to ASCII conversion
        ascii_art = converter.convert_image_to_ascii(args.input_image, output_width=args.width)
        
        # Step 4: Handle output (print to console or save to file)
        if args.output_file:
            output_handler.save_to_text_file(ascii_art, args.output_file)
            print(f"ASCII art saved to {args.output_file}")
        else:
            print(ascii_art) # Print to console if no output file is specified
            
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main() # Run the main function when the script is executed
