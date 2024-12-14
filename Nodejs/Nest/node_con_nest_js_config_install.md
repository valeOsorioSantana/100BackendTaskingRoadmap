¡Bienvenido a Aquicreamos al Archivo! A continuación, te proporcionaré los pasos necesarios para configurar un servidor local usando Docker con Node.js y NestJS.

### Requisitos Previos

1. **Docker**: Asegúrate de tener Docker instalado en tu máquina. Puedes descargarlo desde [aquí](https://www.docker.com/get-started).

2. **Node.js**: Aunque usaremos Docker, es recomendable tener Node.js y npm instalados para desarrollo local y pruebas. Puedes descargarlo desde [aquí](https://nodejs.org/).

### Pasos para Configurar el Proyecto

1. **Crear un nuevo proyecto NestJS**:
   
   Abre una terminal y ejecuta el siguiente comando para crear un nuevo proyecto NestJS. Necesitas tener el CLI de NestJS instalado, así que asegúrate de hacerlo primero.

   ```bash
   npm i -g @nestjs/cli
   nest new nombre-del-proyecto
   ```

   Cambia `nombre-del-proyecto` por el nombre que desees para tu proyecto.

2. **Navegar al directorio del proyecto**:

   ```bash
   cd nombre-del-proyecto
   ```

3. **Crear un archivo `Dockerfile`**:

   En la raíz de tu proyecto, crea un archivo llamado `Dockerfile` y agrega lo siguiente:

   ```dockerfile
   # Usa una imagen base oficial de Node.js
   FROM node:14

   # Establece el directorio de trabajo
   WORKDIR /usr/src/app

   # Copia package.json y package-lock.json
   COPY package*.json ./

   # Instala las dependencias
   RUN npm install

   # Copia el resto de la aplicación
   COPY . .

   # Exponer el puerto en el que corre la aplicación
   EXPOSE 3000

   # Comando para correr la aplicación
   CMD ["npm", "run", "start"]
   ```

4. **Crear un archivo `.dockerignore`**:

   Surete de crear un archivo llamado `.dockerignore` en la raíz del proyecto para excluir archivos innecesarios:

   ```
   node_modules
   npm-debug.log
   dist
   ```

5. **Construir la imagen de Docker**:

   En la terminal, ejecuta el siguiente comando para construir la imagen Docker:

   ```bash
   docker build -t nombre-del-proyecto .
   ```

   Asegúrate de reemplazar `nombre-del-proyecto` por un nombre adecuado.

6. **Ejecutar el contenedor**:

   Después de construir la imagen, puedes ejecutar el contenedor con el siguiente comando:

   ```bash
   docker run -p 3000:3000 nombre-del-proyecto
   ```

   Esto vinculará el puerto 3000 de tu contenedor al puerto 3000 de tu máquina local.

7. **Acceder a la aplicación**:

   Abre un navegador y ve a `http://localhost:3000`. Deberías ver la aplicación NestJS corriendo.

### Notas Adicionales

- Si necesitas producir una versión optimizada de tu aplicación para producción, considera usar `npm run build` y cambiar el CMD en tu Dockerfile para usar el archivo compilado.

- No olvides manejar correctamente las variables de entorno utilizando un archivo `.env` si tu aplicación lo requiere.

Con estos pasos, deberías tener un servidor local corriendo tu aplicación NestJS dentro de Docker. Si necesitas más ayuda o tienes alguna pregunta, ¡no dudes en preguntar!