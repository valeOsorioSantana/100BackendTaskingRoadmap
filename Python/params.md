En Django, puedes leer parámetros de consulta (query parameters) y parámetros de ruta (path parameters) utilizando la vista que estás implementando. A continuación, te muestro cómo hacerlo para ambos tipos de parámetros:

### 1. Leer parámetros de consulta (query parameters)

Los parámetros de consulta son aquellos que se envían en la URL después del signo de pregunta (`?`). Puedes acceder a estos parámetros usando `request.GET` en tus vistas.

#### Ejemplo:
Supongamos que tienes una URL como esta: `/mi-vista/?nombre=Juan&edad=30`.

```python
from django.http import JsonResponse
from django.views import View

class MiVista(View):
    def get(self, request):
        nombre = request.GET.get('nombre')
        edad = request.GET.get('edad')

        return JsonResponse({'nombre': nombre, 'edad': edad})
```

### 2. Leer parámetros de ruta (path parameters)

Los parámetros de ruta son aquellos que se definen en la URL como parte de la ruta misma. Puedes acceder a estos parámetros usando `request.path_params` en las vistas basadas en clase o usando el argumento de la vista.

#### Ejemplo:
Supongamos que tienes una URL como esta: `/mi-vista/123/`.

Primero, asegúrate de definir la URL en tu archivo `urls.py` con un parámetro.

```python
from django.urls import path
from .views import MiVista

urlpatterns = [
    path('mi-vista/<int:id>/', MiVista.as_view(), name='mi-vista'),
]
```

Ahora, en la vista, puedes acceder al parámetro de ruta de la siguiente manera:

```python
from django.http import JsonResponse
from django.views import View

class MiVista(View):
    def get(self, request, id):
        # Aquí `id` es el parámetro de ruta que has capturado
        return JsonResponse({'id': id})
```

### Resumen

- Para acceder a **query parameters**: utiliza `request.GET`.
- Para acceder a **path parameters**: simplemente incluye el parámetro como argumento en tu método de vista.

Con estos ejemplos, deberías poder manejar tanto los parámetros de consulta como los de ruta en tus vistas de Django.