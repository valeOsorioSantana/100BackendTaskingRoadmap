¡Bienvenido! Aquí tienes las instrucciones para leer parámetros de consulta (`query params`) y de ruta (`path params`) en una aplicación de Kotlin con Spring Boot:

### Requisitos Previos
Asegúrate de tener un proyecto de Spring Boot configurado con las dependencias necesarias para Kotlin. Generalmente, necesitarás las siguientes dependencias en tu archivo `build.gradle.kts`:

```kotlin
dependencies {
    implementation("org.springframework.boot:spring-boot-starter-web")
    implementation("org.jetbrains.kotlin:kotlin-reflect")
    implementation("org.jetbrains.kotlin:kotlin-stdlib-jdk8")
    ...
}
```

### Lectura de Path Params

1. **Definir la Ruta en el Controlador**:
   Puedes utilizar anotaciones de Spring para definir la ruta y los parámetros. Por ejemplo, si deseas capturar un ID de un recurso.

```kotlin
import org.springframework.web.bind.annotation.*

@RestController
@RequestMapping("/api")
class MyController {

    @GetMapping("/items/{id}")
    fun getItemById(@PathVariable id: Long): String {
        return "Item con ID: $id"
    }
}
```

En este ejemplo, el ID se captura como un parámetro de ruta a través de la anotación `@PathVariable`.

### Lectura de Query Params

2. **Definir los Parámetros de Consulta**:
   Puedes definir los parámetros de consulta de la siguiente manera:

```kotlin
@CrossOrigin
@GetMapping("/items")
fun getItems(@RequestParam(required = false) category: String?, @RequestParam(required = false) sort: String?): String {
    return "Categoría: $category, Ordenar por: $sort"
}
```

Aquí, `category` y `sort` son parámetros de consulta que se pueden pasar en la URL como `?category=books&sort=asc`.

### Ejemplo Completo

Aquí tienes un ejemplo completo de un controlador que maneja ambos tipos de parámetros:

```kotlin
import org.springframework.web.bind.annotation.*

@RestController
@RequestMapping("/api")
class MyController {

    @GetMapping("/items/{id}")
    fun getItemById(@PathVariable id: Long): String {
        return "Item con ID: $id"
    }

    @GetMapping("/items")
    fun getItems(@RequestParam(required = false) category: String?, @RequestParam(required = false) sort: String?): String {
        return "Categoría: $category, Ordenar por: $sort"
    }
}
```

### Ejecución

Para probar los endpoints, puedes usar herramientas como Postman o simplemente tu navegador (para los parámetros de consulta).

- Ruta con path param: `GET http://localhost:8080/api/items/1`
- Ruta con query params: `GET http://localhost:8080/api/items?category=books&sort=asc`

### Notas Finales
- Asegúrate de tener configurado un servidor embebido (como Tomcat) para servir tu aplicación Spring Boot.
- Consulta la documentación oficial de [Spring](https://docs.spring.io/spring-framework/docs/current/reference/html/web.html#mvc-framework) para más detalles y opciones avanzadas.

¡Espero que esto te ayude a empezar con Kotlin y Spring Boot! Si tienes más preguntas, no dudes en preguntar.