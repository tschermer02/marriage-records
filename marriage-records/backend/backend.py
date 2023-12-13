from flask import Flask, request, jsonify
import subprocess
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, resources={r"/execute": {"origins": "http://localhost:5173"}})
CORS(app, resources={r"/upload": {"origins": "http://localhost:5173"}})

# Function to execute code from a Python script
def execute_code_in_script(code):
    try:
        # Write the code to a temporary Python script
        with open('MarriageRecords.py', 'w') as f:
            f.write(code)

        # Execute the Python script using subprocess
        process = subprocess.Popen(['python', 'temp_script.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

        # Check for errors
        if error:
            return jsonify({'error': error.decode('utf-8')}), 500
        else:
            return jsonify({'result': output.decode('utf-8')})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/execute', methods=['POST'])
def execute_code():
    code = request.json['code']

    try:
        # Execute code from the Python script
        result = execute_code_in_script(code)
        return result
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/upload', methods=['POST'])
def upload_files():
    uploaded_files = request.files.getlist('files')
    save_directory = 'test_image_folder/'  # Adjust the path
    uploaded_filenames = []
    
    # Get the absolute path of the save_directory
    abs_save_directory = os.path.abspath(save_directory)
    print(f"Saving files to: {abs_save_directory}")  # Print the absolute path to the console
    
    for file in uploaded_files:
        file.save(os.path.join(save_directory, file.filename))  # Using os.path.join for better path handling
        uploaded_filenames.append(file.filename)
    
    return jsonify({'message': 'Files uploaded successfully', 'uploaded_files': uploaded_filenames, 'save_path': abs_save_directory})

if __name__ == '__main__':
    app.run(debug=True)
