¡Bienvenido! Vamos a configurar un servidor local utilizando Docker para una aplicación en Python con FastAPI. A continuación, te proporciono una guía paso a paso para hacerlo.

### Paso 1: Instalación de Docker

Antes de comenzar, asegúrate de que Docker esté instalado en tu sistema. Puedes descargarlo e instalarlo desde [Docker Hub](https://www.docker.com/products/docker-desktop).

### Paso 2: Crear la estructura de la aplicación

Crea un directorio para tu proyecto y navega a él. Dentro, crea los siguientes archivos:

```
mi_proyecto/
│
├── app/
│   ├── main.py
│   └── requirements.txt
│
└── Dockerfile
```

### Paso 3: Escribir el código de FastAPI

En el archivo `main.py`, ingresa el siguiente código:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}
```

### Paso 4: Crear el archivo de dependencias

En `requirements.txt`, agrega las siguientes dependencias:

```
fastapi
uvicorn
```

### Paso 5: Configurar el Dockerfile

En el archivo `Dockerfile`, agrega lo siguiente:

```dockerfile
# Usa la imagen oficial de Python como base
FROM python:3.9

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requisitos y cámbiale nombre dentro del contenedor
COPY app/requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación
COPY app/ .

# Expone el puerto que usará FastAPI
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Paso 6: Construir la imagen de Docker

Navega al directorio donde se encuentra tu `Dockerfile` en la línea de comandos y ejecuta el siguiente comando para construir la imagen Docker:

```bash
docker build -t mi_fastapi_app .
```

### Paso 7: Ejecutar el contenedor

Después de que la imagen se haya construido correctamente, ejecuta el contenedor con el siguiente comando:

```bash
docker run -d --name fastapi_container -p 8000:8000 mi_fastapi_app
```

### Paso 8: Acceder a la aplicación

Una vez que el contenedor esté en ejecución, puedes acceder a tu aplicación FastAPI en:

```
http://localhost:8000
```

Además, puedes acceder a la documentación automática de la API en:

```
http://localhost:8000/docs
```

### Paso 9: Detener y eliminar el contenedor (opcional)

Si deseas detener y eliminar el contenedor, puedes usar los siguientes comandos:

```bash
docker stop fastapi_container
docker rm fastapi_container
```

¡Y eso es todo! Ahora tienes un servidor local que ejecuta una aplicación FastAPI dentro de Docker. Si tienes más preguntas o necesitas ayuda adicional, no dudes en preguntar.