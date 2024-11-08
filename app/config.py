import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'tu-clave-secreta'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/app.db'
    UPLOAD_FOLDER = os.path.join('uploads')
    TEMP_FOLDER = os.path.join('temp')
    
    # Asegúrate de que las carpetas existan
    @staticmethod
    def init_app(app):
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        os.makedirs(app.config['TEMP_FOLDER'], exist_ok=True)