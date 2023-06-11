from flask import current_app
from werkzeug.utils import secure_filename
import os
import uuid

# Get the root folder of your project
PROJECT_FOLDER = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Set the UPLOAD_FOLDER relative to the project root
# UPLOAD_FOLDER = os.path.join(PROJECT_FOLDER, 'House-Explorer_Web-App', 'views', 'UPLOADS')

# Set the UPLOAD_FOLDER relative to the project root
UPLOAD_FOLDER = os.path.join(PROJECT_FOLDER, 'House-Explorer_Web-App', 'views', 'static', 'UPLOADS')

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}

def allowed_file(filename):
    # Check if the file has an allowed extension
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def generate_unique_filename(filename):
    # Generate a unique filename using UUID
    _, ext = os.path.splitext(filename)
    unique_filename = str(uuid.uuid4()) + ext
    return unique_filename

def save_file(file):
    # Create the UPLOAD_FOLDER if it doesn't exist
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    
    # Save the file with a unique filename in the UPLOAD_FOLDER
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        unique_filename = generate_unique_filename(filename)
        file_path = os.path.join(UPLOAD_FOLDER, unique_filename)
        file.save(os.path.join(current_app.root_path, file_path))
        return file_path
    else:
        raise ValueError('Invalid file format.')