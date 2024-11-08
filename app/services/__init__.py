"""
Servicios de la aplicación de generación de certificados.

Este paquete contiene los servicios principales de la aplicación, incluyendo:
- Generador de certificados
- Procesamiento de archivos
- Generación de PDFs

Uso típico:
    from app.services import CertificateGenerator
    
    generator = CertificateGenerator(
        excel_path='ruta/al/excel',
        template_path='ruta/a/plantilla',
        output_folder='ruta/salida'
    )
    generator.generate_all()
"""

import logging
from app.services.certificate_generator import CertificateGenerator

# Configuración del logger para los servicios
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Handler para archivo
file_handler = logging.FileHandler('services.log')
file_handler.setLevel(logging.INFO)

# Handler para consola
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Formato del log
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Agregar handlers al logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Exponer las clases principales
__all__ = ['CertificateGenerator']

# Metadatos del paquete
__version__ = '1.0.0'
__author__ = 'Tu Nombre'
__email__ = 'tu@email.com'

# Configuraciones por defecto
DEFAULT_CONFIG = {
    'font_size': 40,
    'font_color': '#280384',
    'spacing': -3
}

def get_version():
    """Retorna la versión actual del paquete de servicios."""
    return __version__

def get_default_config():
    """Retorna la configuración por defecto de los servicios."""
    return DEFAULT_CONFIG.copy()

# Log de inicialización
logger.info(f'Servicios inicializados - Versión {__version__}')