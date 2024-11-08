import os
from pathlib import Path

class Config:
    # Base directory of the application
    BASE_DIR = Path(__file__).resolve().parent.parent
    
    # Flask configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    
    # File upload configuration
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
    TEMP_FOLDER = os.path.join(BASE_DIR, 'temp')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    
    # Allowed file extensions
    ALLOWED_EXTENSIONS = {
        'excel': {'xlsx', 'xls'},
        'image': {'png', 'jpg', 'jpeg'}
    }