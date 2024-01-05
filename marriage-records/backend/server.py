from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/extract', methods=['POST'])
def perform_extraction():
    # Logic for performing extraction here
    try:
        # Your extraction logic here
        return jsonify({"message": "Extraction successful"})
    except Exception as e:
        return jsonify({"message": f"Extraction failed: {str(e)}"}), 500

@app.route('/upload', methods=['POST'])
def upload_files():
    uploaded_files = request.files.getlist("file")

    if len(uploaded_files) == 0:
        return 'No files uploaded'

    upload_directory = 'test_image_folder'
    
    for file in uploaded_files:
        if file.filename == '':
            return 'No selected file'
        file.save(os.path.join(upload_directory, file.filename))

    return 'Files uploaded successfully'

if __name__ == "__main__":
    app.run(debug=True)
