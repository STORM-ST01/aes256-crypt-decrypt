# Proyecto: Cifrado y Descifrado de Imágenes DICOM con AES-256-GCM

## Descripción
Este proyecto proporciona un script en Python para cifrar y descifrar imágenes **DICOM** utilizando el algoritmo de cifrado simétrico **AES-256-GCM**. Se garantiza la confidencialidad e integridad de los datos mediante autenticación de mensajes.

## Instalación y Configuración
Para ejecutar este proyecto correctamente, es recomendable utilizar un **entorno virtual** de Python.

### 1️⃣ Crear y activar el entorno virtual
#### **Windows**
```sh
python -m venv venv
venv\Scripts\activate
```

#### **Linux / macOS**
```sh
python -m venv venv
source venv/bin/activate
```

### 2️⃣ Instalar las dependencias
Asegúrate de instalar los paquetes necesarios con:
```sh
pip install -r requirements.txt
```

## Uso del Script
### **Ejecutar el cifrado y descifrado**
```sh
python aes256.py
```

El script procesará automáticamente los archivos **DICOM** indicados en su configuración y mostrará mensajes en la terminal indicando el éxito del cifrado, descifrado y verificación de integridad.

## Archivos Requeridos
Asegúrate de tener las imágenes DICOM en la carpeta correspondiente y que el script tenga la ruta correcta. Los archivos esperados son:

Si los archivos no existen, el script mostrará una advertencia.


