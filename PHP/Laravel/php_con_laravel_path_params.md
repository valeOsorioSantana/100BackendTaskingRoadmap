¡Bienvenido a Aquicreamos al Archivo! Aquí tienes las instrucciones para leer parámetros de consulta (`query params`) y de ruta (`path params`) en PHP con Laravel:

### Leer Parámetros de Ruta (`Path Params`)

1. **Definir la Ruta**: En el archivo de rutas (`routes/web.php` o `routes/api.php`), puedes definir una ruta que incluya parámetros. Por ejemplo:

   ```php
   Route::get('/usuarios/{id}', 'UsuarioController@mostrar');
   ```

   En este caso, `{id}` es un parámetro de ruta.

2. **Acceder al Parámetro en el Controlador**: En el controlador correspondiente, puedes acceder al parámetro pasado en la ruta de la siguiente manera:

   ```php
   class UsuarioController extends Controller
   {
       public function mostrar($id)
       {
           // Aquí puedes utilizar el parámetro $id
           return "Mostrando usuario con ID: " . $id;
       }
   }
   ```

### Leer Parámetros de Consulta (`Query Params`)

1. **Definir la Ruta**: No es necesario hacer nada especial en la ruta para los parámetros de consulta. Solo necesitas asegurarte de tener una ruta definida. Por ejemplo:

   ```php
   Route::get('/usuarios', 'UsuarioController@listar');
   ```

2. **Acceder a los Parámetros de Consulta en el Controlador**: Puedes acceder a los parámetros de consulta usando el objeto `Request` de Laravel que se puede inyectar en el método del controlador. Por ejemplo:

   ```php
   use Illuminate\Http\Request;

   class UsuarioController extends Controller
   {
       public function listar(Request $request)
       {
           // Acceder a los parámetros de consulta
           $nombre = $request->query('nombre');
           $edad = $request->query('edad');

           return "Lista de usuarios filtrados por nombre: $nombre y edad: $edad";
       }
   }
   ```

3. **Ejemplo de URL**: Para acceder a esta acción podrías usar una URL como:

   ```
   http://tu-sitio.com/usuarios?nombre=Juan&edad=30
   ```

### Resumen

- **Parámetros de ruta** se definen en la URL y se acceden como argumentos en el controlador.
- **Parámetros de consulta** se envían en la URL, después del signo de interrogación (?), y se acceden utilizando el objeto `Request` en el controlador.

¡Espero que esta información te sea útil! Si necesitas más detalles o ejemplos, ¡no dudes en preguntar!