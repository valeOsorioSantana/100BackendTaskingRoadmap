¡Bienvenido! A continuación, te proporcionaré instrucciones sobre cómo leer parámetros de consulta (`query params`) y de ruta (`path params`) utilizando Node.js con el framework Express.

### 1. Instalación de Express

Si aún no tienes Express instalado, primero debes crear un proyecto de Node.js e instalar Express. En la terminal, ejecuta:

```bash
mkdir mi_proyecto
cd mi_proyecto
npm init -y
npm install express
```

### 2. Configuración básica de un servidor Express

Crea un archivo llamado `app.js` y agrega el siguiente código para configurar un servidor básico:

```javascript
const express = require('express');
const app = express();
const PORT = 3000;

// Definir la ruta raíz del servidor
app.get('/', (req, res) => {
    res.send('¡Hola, mundo!');
});

// Iniciar el servidor
app.listen(PORT, () => {
    console.log(`Servidor escuchando en http://localhost:${PORT}`);
});
```

### 3. Leer Parámetros de Ruta (Path Params)

Los parámetros de ruta se definen en la ruta utilizando `:`. Por ejemplo, si deseas capturar un parámetro `id`, puedes hacerlo así:

```javascript
app.get('/usuario/:id', (req, res) => {
    const usuarioId = req.params.id;
    res.send(`Usuario ID: ${usuarioId}`);
});
```

### 4. Leer Parámetros de Consulta (Query Params)

Los parámetros de consulta se envían generalmente después de un signo de interrogación `?` en la URL. Puedes acceder a ellos usando `req.query`. Por ejemplo:

```javascript
app.get('/buscar', (req, res) => {
    const nombre = req.query.nombre; // Ejemplo de nombre como parámetro de consulta
    res.send(`Buscando usuario con nombre: ${nombre}`);
});
```

### 5. Ejemplo Completo

Aquí tienes un ejemplo completo que combina ambos tipos de parámetros:

```javascript
const express = require('express');
const app = express();
const PORT = 3000;

// Ruta para obtener usuario por ID
app.get('/usuario/:id', (req, res) => {
    const usuarioId = req.params.id;
    res.send(`Usuario ID: ${usuarioId}`);
});

// Ruta para buscar usuario por nombre
app.get('/buscar', (req, res) => {
    const nombre = req.query.nombre;
    res.send(`Buscando usuario con nombre: ${nombre}`);
});

// Iniciar el servidor
app.listen(PORT, () => {
    console.log(`Servidor escuchando en http://localhost:${PORT}`);
});
```

### 6. Probar tu Aplicación

Puedes probar tu aplicación utilizando un navegador o herramientas como Postman:

- Para la ruta de usuario: `http://localhost:3000/usuario/123` (donde `123` es el ID del usuario que deseas leer).
- Para la búsqueda: `http://localhost:3000/buscar?nombre=Juan` (donde `Juan` es el nombre que deseas buscar).

¡Y eso es todo! Ahora puedes leer tanto parámetros de ruta como parámetros de consulta en tu aplicación Express. Si tienes alguna pregunta adicional, no dudes en preguntar.