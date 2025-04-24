import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file_name = file.filename
    upload_path = os.path.join(os.getcwd(), 'uploads')
    
    if not os.path.exists(upload_path):
        os.makedirs(upload_path)
    
    file_path = os.path.join(upload_path, file_name)
    
    # Save the file to the uploads directory
    file.save(file_path)

    return "File uploaded successfully", 200

if __name__ == '__main__':
    app.run(debug=True)
