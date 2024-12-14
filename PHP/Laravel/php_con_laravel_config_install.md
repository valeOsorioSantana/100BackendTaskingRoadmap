¡Bienvenido a Aquicreamos al Archivo! Aquí tienes una guía paso a paso para configurar un servidor local utilizando Docker para un proyecto de PHP con Laravel.

### Paso 1: Instalación de Docker

1. **Descarga e instala Docker Desktop**:
   - Ve a [la página oficial de Docker](https://www.docker.com/products/docker-desktop).
   - Descarga la versión para tu sistema operativo (Windows/Mac/Linux).
   - Sigue las instrucciones de instalación.

2. **Verifica la instalación**:
   - Abre la terminal y ejecuta el siguiente comando:
     ```bash
     docker --version
     ```
   - Deberías ver la versión de Docker instalada.

### Paso 2: Crear un nuevo proyecto de Laravel

1. **Instalar Composer** (si no lo tienes ya):
   - Ve a [la página oficial de Composer](https://getcomposer.org/download/) y sigue las instrucciones.

2. **Crear un nuevo proyecto de Laravel**:
   - En la terminal, navega a la carpeta donde deseas crear tu proyecto y ejecuta:
     ```bash
     composer create-project --prefer-dist laravel/laravel nombre_del_proyecto
     ```
   - Cambia `nombre_del_proyecto` por el nombre de tu elección.

### Paso 3: Configuración de Docker

1. **Crear un archivo `Dockerfile`** en la raíz de tu proyecto (dentro de `nombre_del_proyecto`):
   ```dockerfile
   # Usamos la imagen base de PHP
   FROM php:8.0-fpm

   # Instalar extensiones necesarias
   RUN docker-php-ext-install pdo pdo_mysql

   # Configurar el directorio de trabajo
   WORKDIR /var/www

   # Copiar el contenido del proyecto
   COPY . .

   # Exponer el puerto que estará escuchando el contenedor
   EXPOSE 9000
   ```

2. **Crear un archivo `docker-compose.yml`** en la raíz de tu proyecto:
   ```yaml
   version: '3.8'

   services:
     web:
       build:
         context: .
         dockerfile: Dockerfile
       ports:
         - "8000:9000"
       volumes:
         - .:/var/www
       networks:
         - laravel_network

   networks:
     laravel_network:
       driver: bridge
   ```

### Paso 4: Levantar los contenedores

1. **Navegar al directorio del proyecto**:
   ```bash
   cd nombre_del_proyecto
   ```

2. **Construir y correr los contenedores**:
   ```bash
   docker-compose up -d
   ```
   - El `-d` ejecuta los contenedores en segundo plano.

### Paso 5: Acceder a tu aplicación

- Abre un navegador y dirígete a `http://localhost:8000`.
- Deberías ver la página de bienvenida de Laravel.

### Paso 6: Ejecutar migraciones

- Para ejecutar migraciones en tu base de datos, puedes usar el comando:
  ```bash
  docker-compose exec web php artisan migrate
  ```

### Paso 7: Detener y eliminar contenedores

- Para detener y eliminar los contenedores, ejecuta:
  ```bash
  docker-compose down
  ```

### Notas adicionales

- Asegúrate de que la carpeta de tu proyecto tenga los permisos adecuados para que Docker los maneje correctamente.
- Puedes personalizar el `Dockerfile` y `docker-compose.yml` según las necesidades de tu aplicación.

¡Y eso es todo! Con estos pasos, deberías tener un entorno local de desarrollo para Laravel corriendo en Docker. Si tienes alguna pregunta o necesitas más detalles, no dudes en preguntar.