from flask import render_template, current_app, jsonify, make_response
from app.main.forms import CertificateGeneratorForm
from app.services.certificate_generator import CertificateGenerator
from app.main import main_bp  # Importar el Blueprint desde __init__.py
import os
from datetime import datetime
import zipfile
from io import BytesIO
from urllib.parse import quote

@main_bp.route('/', methods=['GET', 'POST'])
def upload_file():
    form = CertificateGeneratorForm()
    
    if form.validate_on_submit():
        try:
            # Generate timestamp for unique filenames
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            
            # Save files temporarily
            excel_path = os.path.join(
                current_app.config['UPLOAD_FOLDER'],
                f'datos_{timestamp}.xlsx'
            )
            template_path = os.path.join(
                current_app.config['UPLOAD_FOLDER'],
                f'plantilla_{timestamp}.png'
            )
            output_folder = os.path.join(
                current_app.config['TEMP_FOLDER'],
                f'certificados_{timestamp}'
            )
            
            form.excel_file.data.save(excel_path)
            form.template_file.data.save(template_path)
            
            # Create output folder
            os.makedirs(output_folder, exist_ok=True)
            
            # Generate certificates
            generator = CertificateGenerator(
                excel_path=excel_path,
                template_path=template_path,
                output_folder=output_folder
            )
            generator.generate_all()
            
            # Create ZIP file in memory
            memory_file = BytesIO()
            with zipfile.ZipFile(memory_file, 'w', zipfile.ZIP_DEFLATED) as zf:
                for root, dirs, files in os.walk(output_folder):
                    for file in files:
                        if file.endswith('.pdf'):
                            file_path = os.path.join(root, file)
                            arcname = os.path.basename(file_path)
                            zf.write(file_path, arcname)
            
            # Clean up temporary files
            cleanup_files([excel_path, template_path, output_folder])
            
            # Prepare file for download
            memory_file.seek(0)
            response = make_response(memory_file.getvalue())
            response.headers['Content-Type'] = 'application/zip'
            response.headers['Content-Disposition'] = f'attachment; filename=certificados_{timestamp}.zip'
            
            return response
            
            
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    return render_template('main/upload.html', form=form)

def cleanup_files(paths):
    """Clean up temporary files and folders"""
    for path in paths:
        if os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for file in files:
                    os.remove(os.path.join(root, file))
            os.rmdir(path)
        elif os.path.isfile(path):
            os.remove(path)
            
