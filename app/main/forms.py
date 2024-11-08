from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField

class CertificateGeneratorForm(FlaskForm):
    excel_file = FileField('Archivo Excel',
        validators=[
            FileRequired(),
            FileAllowed(['xlsx', 'xls'], 'Solo archivos Excel!')
        ]
    )
    template_file = FileField('Plantilla',
        validators=[
            FileRequired(),
            FileAllowed(['png', 'jpg', 'jpeg'], 'Solo imágenes!')
        ]
    )
    submit = SubmitField('Generar Certificados')