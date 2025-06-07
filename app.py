from flask import Flask, render_template, request, send_from_directory
from src.ascii_converter import AsciiConverter
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_image():
    if 'image' not in request.files:
        return 'No image file part in the request', 400
    
    file = request.files['image']
    if file.filename == '':
        return 'No selected file', 400
    
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        
        converter = AsciiConverter()
        # You can add options for width or character set here if desired
        # For simplicity, we'll use a default width for now
        output_width = request.form.get('width', type=int, default=100)
        
        try:
            ascii_art = converter.convert_image_to_ascii(filepath, output_width=output_width)
            # Clean up the uploaded file after conversion
            os.remove(filepath)
            return render_template('ascii_display.html', ascii_art=ascii_art)
        except FileNotFoundError:
            return "Error: Image file not found.", 404
        except Exception as e:
            return f"An error occurred during conversion: {e}", 500

def convert_to_uppercase(text):
    return text.upper()

if __name__ == '__main__':
    app.run(debug=True)
