from flask import Flask
from app.config import Config
from app.main import main_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register blueprints
    app.register_blueprint(main_bp)

    # Create necessary folders
    with app.app_context():
        import os
        for folder in [app.config['UPLOAD_FOLDER'], app.config['TEMP_FOLDER']]:
            if not os.path.exists(folder):
                os.makedirs(folder)

    return app