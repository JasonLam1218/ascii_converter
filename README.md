# ASCII Image Converter

This project provides a command-line interface (CLI) application to convert images into ASCII art.

## Project Overview

The system takes an input image, processes it to extract brightness information, maps these brightness values to a set of ASCII characters, and then outputs the resulting ASCII art to the terminal or a specified text file.

## Features

*   **Image Loading & Processing**: Loads various image formats, converts them to grayscale, and resizes them for optimal ASCII art generation.
*   **Customizable Output**: Allows setting the output width of the ASCII art.
*   **Flexible Output**: Display ASCII art directly in the terminal or save it to a `.txt` file.
*   **Web Interface**: Provides a user-friendly web interface for uploading images and viewing ASCII art in a browser.

## Installation

To set up and run this project, follow these steps:

1.  **Clone the repository** (if you haven't already):
    ```bash
    git clone https://github.com/JasonLam1218/ascii_converter.git
    cd ascii_converter
    ```

2.  **Create and Activate a Virtual Environment**:
    It's highly recommended to use a virtual environment to manage project dependencies.
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**:
    With the virtual environment activated, install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Once installed, you can run the ASCII image converter from your terminal.

**Prepare an Image**: Place an image file (e.g., `my_image.jpg`, `picture.png`) in your project's root directory or use the full path to any image on your system.

**Run the Application**:

Use the `python3 -m src.main` command followed by the image path and optional arguments.

*   **Display ASCII art directly in the terminal**:
    ```bash
    python3 -m src.main /path/to/your/image.jpg
    ```
    (Replace `/path/to/your/image.jpg` with the actual path to your image file, e.g., `my_image.jpg` if it's in the project root, or `/Users/jasonlam/Pictures/cat.jpeg` for a specific file.)

*   **Save ASCII art to a file**:
    To convert an image and save the ASCII art to a text file (e.g., `output.txt` in your current directory), use the `-o` or `--output_file` option:
    ```bash
    python3 -m src.main /path/to/your/image.jpg -o output.txt
    ```

*   **Specify output width**:
    You can control the width of the generated ASCII art using the `-w` or `--width` option (default is 100 characters):
    ```bash
    python3 -m src.main /path/to/your/image.jpg -w 200
    ```

### Web Interface Usage

To use the web interface, ensure your virtual environment is activated and then run the `app.py` Flask application:

1.  **Activate your virtual environment** (if not already active):
    ```bash
    source venv/bin/activate
    ```

2.  **Run the Flask application**:
    ```bash
    python app.py
    ```
    You should see output indicating that the Flask development server is running, usually on `http://127.0.0.1:5000` or `http://localhost:5000`.

3.  **Access the web interface**:
    Open your web browser and navigate to the address provided in the terminal (e.g., `http://127.0.0.1:5000`). You will be able to upload an image and see the ASCII art directly in your browser.

## Project Structure

*   `src/main.py`: The command-line interface (CLI) entry point for the application.
*   `src/image_processor.py`: Handles loading, grayscale conversion, resizing, and pixel brightness extraction from images.
*   `src/character_mapper.py`: Contains logic to map image brightness values to ASCII characters.
*   `src/ascii_converter.py`: Orchestrates the image processing and character mapping to generate the final ASCII art.
*   `src/output_handler.py`: Manages saving the generated ASCII art to text files.
*   `requirements.txt`: Lists the Python dependencies required for the project (e.g., Pillow).
*   `app.py`: The Flask web application entry point for the web interface.
