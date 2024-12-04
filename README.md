# Generador Automático de Certificados

Una aplicación web robusta desarrollada con Flask que permite generar certificados personalizados de forma automática a partir de una plantilla y datos en Excel.

## 🌟 Características

- Generación masiva de certificados personalizados
- Interfaz web intuitiva para cargar archivos
- Procesamiento asíncrono de certificados
- Descarga automática de certificados en formato ZIP
- Sistema de notificaciones en tiempo real
- Diseño responsive y moderno
- Soporte para múltiples formatos de plantilla (PNG, JPG, JPEG)
- Logging completo de operaciones

## 🛠️ Tecnologías Utilizadas

- **Backend**: Python 3.10+ con Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Procesamiento de Imágenes**: Pillow
- **Generación de PDFs**: ReportLab
- **Procesamiento de Datos**: Pandas
- **Contenedorización**: Docker

## 📋 Prerrequisitos

- Python 3.10 o superior
- Docker (opcional)
- Fuentes necesarias (incluidas en el proyecto)

## 🚀 Instalación y Configuración

### Instalación Local

1. Clonar el repositorio:
```bash
git clone https://github.com/WhitneySt/web-certificate-generator.git
cd web-certificate-generator
```

2. Crear y activar un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno (opcional):
```bash
export SECRET_KEY="tu-clave-secreta"
```

5. Ejecutar la aplicación:
```bash
python run.py
```

### Instalación con Docker

1. Construir la imagen:
```bash
docker build -t certificate-generator .
```

2. Ejecutar el contenedor:
```bash
docker run -p 10000:10000 certificate-generator
```

## 📁 Estructura del Proyecto

```
web-certificate-generator/
├── app/                      # Aplicación principal
│   ├── main/                # Blueprint principal
│   │   ├── forms.py        # Formularios
│   │   └── routes.py       # Rutas
│   ├── services/           # Servicios de la aplicación
│   │   └── certificate_generator.py
│   ├── static/             # Archivos estáticos
│   └── templates/          # Plantillas HTML
├── fonts/                   # Fuentes para certificados
├── instance/               # Datos de instancia
├── temp/                   # Archivos temporales
├── uploads/                # Archivos subidos
└── requirements.txt        # Dependencias
```

## 📝 Uso

1. Acceder a la aplicación web en `http://localhost:10000`
2. Subir archivo Excel con los datos siguiendo este formato:
   - Columna `nombre_completo`: Nombre del participante
   - Columna `identificacion`: Número de identificación
3. Subir imagen de plantilla (PNG, JPG, JPEG)
4. Hacer clic en "Generar Certificados"
5. Esperar la descarga automática del archivo ZIP con los certificados

## 🔧 Configuración Avanzada

### Personalización de Estilos

Los estilos de los certificados se pueden configurar en `certificate_generator.py`:

```python
self.styles = {
    'name': {
        'font': 'RobotoMono-Bold.ttf',
        'size': 50,
        'color': '#280384',
        'position_y': 250,
        'spacing': -3
    }
    # ... más configuraciones
}
```

### Configuración del Servidor

Modificar `config.py` para ajustar:
- Carpetas de carga y temporales
- Configuración de base de datos
- Claves secretas
- Otros parámetros de la aplicación

## 📊 Logging

La aplicación mantiene un registro detallado de operaciones en `services.log`:
- Generación de certificados
- Errores y excepciones
- Información de procesamiento

## 🔒 Seguridad

- Validación de tipos de archivo
- Limpieza automática de archivos temporales
- Nombres de archivo seguros con timestamps
- Manejo seguro de rutas de archivo

## 🤝 Contribución

1. Fork el repositorio
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE para detalles.

## ✨ Autor

Whitney Stevenson - [GitHub Profile](https://github.com/WhitneySt)

## 🙏 Agradecimientos

- Flask y su comunidad
- Contribuidores de las bibliotecas utilizadas
- Todos los que han aportado al proyecto