# Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements primero para aprovechar la caché de Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY . .

# Crear directorios necesarios
RUN mkdir -p uploads temp instance

# Establecer permisos
RUN chmod -R 755 uploads temp instance

# Exponer el puerto
EXPOSE 10000

# Comando para ejecutar la aplicación
CMD gunicorn --bind 0.0.0.0:10000 run:app