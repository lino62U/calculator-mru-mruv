#!/bin/bash

# Nombre del entorno virtual
VENV_DIR="ven"

# Directorio donde está ubicado el código principal
SOURCE_DIR="source"

# Archivo principal a ejecutar
MAIN_FILE="main.py"

# Archivo de requerimientos
REQUIREMENTS_FILE="requirements.txt"

# Función para crear y activar el entorno virtual si no existe
setup_venv() {
    if [ ! -d "$VENV_DIR" ]; then
        echo "El entorno virtual no existe. Creándolo..."
        python3 -m venv $VENV_DIR
    fi
    
    # Verificar si el entorno virtual ya está activado
    if [ -z "$VIRTUAL_ENV" ]; then
        echo "Activando el entorno virtual..."
        source $VENV_DIR/bin/activate
    else
        echo "El entorno virtual ya está activado."
    fi

    # Instalar dependencias desde el archivo requirements.txt
    if [ -f "$REQUIREMENTS_FILE" ]; then
        echo "Instalando dependencias desde $REQUIREMENTS_FILE..."
        pip install -r $REQUIREMENTS_FILE
    else
        echo "El archivo $REQUIREMENTS_FILE no existe. No se instalarán dependencias adicionales."
    fi
}

# Configuración del entorno virtual
setup_venv

# Navegar al directorio fuente
cd $SOURCE_DIR || { echo "El directorio $SOURCE_DIR no existe."; exit 1; }

# Ejecutar el archivo principal de Python
echo "Ejecutando $MAIN_FILE..."
python3 $MAIN_FILE  # Aquí se ejecuta directamente el archivo main.py
