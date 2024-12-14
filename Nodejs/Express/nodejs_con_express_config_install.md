¡Bienvenido a Aquicreamos al Archivo! A continuación, te proporcionaré las instrucciones necesarias para configurar un servidor local utilizando Docker, Node.js y Express.

### Paso 1: Instalar Docker

1. **Descargar e instalar Docker**: Dirígete a [la página de descargas de Docker](https://www.docker.com/products/docker-desktop) y sigue las instrucciones para instalar Docker Desktop en tu sistema operativo (Windows, macOS, o Linux).

2. **Verificar la instalación**: Abre la terminal o línea de comandos y ejecuta:
   ```bash
   docker --version
   ```
   Deberías ver la versión de Docker instalada.

### Paso 2: Crear el proyecto Node.js con Express

1. **Crear un directorio para tu proyecto**:
   ```bash
   mkdir mi-proyecto-express
   cd mi-proyecto-express
   ```

2. **Inicializar un nuevo proyecto de Node.js**:
   ```bash
   npm init -y
   ```

3. **Instalar Express**:
   ```bash
   npm install express
   ```

4. **Crear un archivo `server.js`**:
   ```javascript
   // server.js
   const express = require('express');
   const app = express();
   const PORT = 3000;

   app.get('/', (req, res) => {
       res.send('¡Hola Mundo desde Express!');
   });

   app.listen(PORT, () => {
       console.log(`Servidor corriendo en http://localhost:${PORT}`);
   });
   ```

### Paso 3: Crear el archivo `Dockerfile`

1. **Crea un archivo llamado `Dockerfile`** en la raíz de tu proyecto:
   ```Dockerfile
   # Usar la imagen oficial de Node.js
   FROM node:14

   # Establecer el directorio de trabajo
   WORKDIR /usr/src/app

   # Copiar package.json y package-lock.json
   COPY package*.json ./

   # Instalar las dependencias
   RUN npm install

   # Copiar el resto del proyecto
   COPY . .

   # Exponer el puerto que utiliza la aplicación
   EXPOSE 3000

   # Comando para iniciar la aplicación
   CMD ["node", "server.js"]
   ```

### Paso 4: Crear un archivo `docker-compose.yml`

1. **Crea un archivo llamado `docker-compose.yml`** en la raíz de tu proyecto:
   ```yaml
   version: '3'
   services:
     app:
       build: .
       ports:
         - "3000:3000"
   ```

### Paso 5: Construir y correr el contenedor

1. **Construir el contenedor**:
   ```bash
   docker-compose build
   ```

2. **Correr el contenedor**:
   ```bash
   docker-compose up
   ```

### Paso 6: Acceder a la aplicación

Abre tu navegador y dirígete a `http://localhost:3000`. Deberías ver el mensaje "¡Hola Mundo desde Express!".

### Notas finales

- Puedes detener el contenedor presionando `Ctrl + C` en la terminal donde está corriendo `docker-compose`.
- Si deseas ejecutar el contenedor en segundo plano, puedes usar `docker-compose up -d`.
- Asegúrate de tener Docker corriendo en tu sistema durante todo el proceso.

¡Espero que estas instrucciones te sean útiles para configurar tu servidor local! Si tienes alguna duda, no dudes en preguntar.