# Fase 1: Fundamentos de Clases y Objetos
🧾 Caso de uso: Registro de Clientes en un sistema de facturación
Regla de negocio: Un cliente debe tener nombre, correo electrónico y un número único de identificación.

Aplicación POO:

Clase: Cliente → Es el plano que define cómo es un cliente.

Objeto: Cada vez que alguien se registra, se crea un objeto Cliente nuevo.

Atributos: nombre, email, idCliente.

Métodos: registrarCliente(), actualizarEmail(), mostrarInfoCliente().

# 🔹 Encapsulamiento
🔐 Caso de uso: Control de acceso a la información del cliente
Regla de negocio: El ID del cliente no puede ser modificado desde fuera del sistema.

Aplicación POO:

Se encapsula el atributo idCliente usando private.

Se expone el método getIdCliente() pero no un setIdCliente().

Otros campos como nombre y correo se exponen con getters y setters validados.

Encapsulación asegura que los datos sensibles no sean manipulados incorrectamente.

# 🔹 Constructores
🏗️ Caso de uso: Creación automática de clientes desde formularios web
Regla de negocio: Un cliente puede ser creado vacío (con constructor por defecto) o con datos desde el inicio (con parámetros).

Aplicación POO:

Constructor vacío → útil para librerías de serialización (JSON, XML).

Constructor con parámetros → útil para creación directa de clientes en la lógica de negocio.

Uso de this para diferenciar entre atributos y parámetros en los métodos y constructores.

# 🔹 Fase 2: Métodos y Lógica de Negocio
⚙️ Caso de uso: Cálculo del valor total de una factura
Regla de negocio: Una factura suma el valor de todos sus productos.

Aplicación POO:

Método calcularTotal() dentro de la clase Factura.

Acepta parámetros como lista de productos y aplica lógica de suma.

Retorna un valor tipo double.

Se puede sobrecargar para calcular con o sin impuestos.

# 🔹 Métodos static y variables static
📊 Caso de uso: Control de cantidad de productos registrados
Regla de negocio: El sistema debe contar cuántos productos han sido agregados sin importar el usuario.

Aplicación POO:

Variable estática contadorProductos.

Método estático getTotalProductos() para consultar sin necesidad de crear un objeto.

# 🔹 Herencia
🧬 Caso de uso: Diferentes tipos de usuarios en una plataforma (Cliente, Admin, Empleado)
Regla de negocio: Todos los usuarios deben poder iniciar sesión, pero cada tipo tiene permisos distintos.

Aplicación POO:

Clase base: Usuario con método login().

Subclases: Cliente, Admin, Empleado, heredan de Usuario.

Uso de super() para inicializar atributos comunes.

Reutilización de lógica para evitar duplicación de código.

# 🔹 Polimorfismo
🎭 Caso de uso: Generar un reporte mensual
Regla de negocio: Dependiendo del tipo de usuario, el reporte cambia (Cliente ve facturas, Admin ve ingresos).

# Aplicación POO:

Método generarReporte() definido en Usuario, sobrescrito en cada subclase.

Se puede tratar cualquier objeto Usuario sin saber si es Cliente o Admin (upcasting).

Uso de super.generarReporte() si se necesita extender lógica anterior.

# 🔹 Abstracción
🧰 Caso de uso: Procesamiento de pagos
Regla de negocio: El sistema debe permitir procesar pagos con múltiples medios (tarjeta, PayPal, efectivo).

Aplicación POO:

Clase abstracta: MetodoPago con métodos como validar() y procesar().

Subclases: PagoTarjeta, PagoPayPal, PagoEfectivo.

Cada subclase implementa su propia lógica.

Se puede usar una lista de MetodoPago para procesar todos por igual (polimorfismo).

📜 Caso de uso adicional con interfaces:
Se define la interfaz Autenticable, implementada por Admin, Cliente, Empleado.

Regla de negocio: Todos deben poder autenticarse, pero la lógica puede cambiar.

# 🔹 Estructuras de Datos y Utilidades
📦 Caso de uso: Gestión de productos en el carrito de compras
Regla de negocio: El carrito debe poder contener múltiples productos únicos y sumarlos.

Aplicación POO:

Usar ArrayList<Producto> para manejar productos.

Iterar con bucles para calcular subtotal.

Usar HashMap<Producto, Integer> para saber cuántas unidades hay por producto.

# 🔹 Clase String
✉️ Caso de uso: Validación de correo electrónico y generación de códigos
Regla de negocio: El sistema debe validar que el correo sea único y tenga formato correcto.

Aplicación POO:

Uso de métodos .contains(), .indexOf(), .substring(), .equals() para validaciones.

Comparación de cadenas con .equals() y no ==.

# 🔹 Clases Wrapper y Autoboxing
📊 Caso de uso: Estadísticas de ventas
Regla de negocio: El sistema debe permitir sumar totales con estructuras como listas de enteros.


Uso de Integer para listas genéricas (List<Integer>).
Autoboxing para convertir de int a Integer automáticamente.

# 🔹 Colecciones: List, Set, Map
📚 Caso de uso: Control de inventario
Regla de negocio:

No se deben duplicar productos → usar Set.
Consultar cantidad disponible por código → usar Map<String, Integer>.
Listar todos los productos → usar List<Producto>.
Aplicación POO:
Uso práctico de colecciones según la necesidad del negocio.


# Luego de esta exploración de las reglas de negocio usando la POO ahora vamos a aprender un poco más de reglas de negocio

🔸 1. Generación de Reportes de Ventas en JSON
Regla de negocio: Al final del día, se debe generar un reporte con todas las ventas y guardarlo en formato JSON para ser enviado por correo.

Conceptos POO:

Clases: Venta, ReporteDiario, Producto.

Método: generarReporteJSON() usando una librería como Gson o Jackson.

Uso de herencia si hay distintos tipos de reportes (diario, mensual).

Serialización de objetos a JSON.

🔸 2. Gestión de Tareas Pendientes con SQLite
Regla de negocio: Los empleados deben tener tareas asignadas. Cada tarea tiene prioridad, fecha límite y estado.

Conceptos POO:

Clases: Empleado, Tarea, BaseDeDatosTareas.

Conexión con SQLite para guardar tareas.

Uso de relaciones 1:N entre empleados y tareas.

CRUD usando JDBC.

🔸 3. Cálculo de Préstamos Bancarios
Regla de negocio: Un cliente puede solicitar un préstamo y el sistema debe calcular la cuota mensual con base en el interés compuesto.

Conceptos POO:

Clase: Prestamo con métodos calcularCuotaMensual(), generarCronogramaPagos().

Atributos: monto, tasa de interés, plazos.

Uso de BigDecimal para cálculos financieros precisos.

🔸 4. Registro de Asistencias en Archivos CSV
Regla de negocio: Un curso debe llevar el control diario de asistencia y guardar esa información en un archivo CSV.

Conceptos POO:

Clase: Estudiante, Clase, Asistencia.

Método: exportarAsistenciaCSV().

Uso de FileWriter, BufferedWriter o OpenCSV.

🔸 5. Generador de Facturas con Fechas y Subtotales
Regla de negocio: Una factura debe incluir la fecha de emisión, los productos vendidos y calcular automáticamente los subtotales e IVA.

Conceptos POO:

Clases: Factura, Producto, Cliente.

Métodos: calcularTotal(), generarFecha().

Uso de LocalDate, DateTimeFormatter y formateo de números.

🔸 6. Validación de Usuarios desde un Archivo JSON
Regla de negocio: Los usuarios deben validarse contra un archivo usuarios.json antes de acceder al sistema.

Conceptos POO:

Clase: Usuario, Autenticador.

Método: validarCredenciales(usuario, clave) usando lectura de JSON.

Cargar una lista de usuarios como objetos desde el archivo.

🔸 7. Sistema de Reservas para Consultorio Médico
Regla de negocio: Cada médico tiene una agenda y los pacientes deben agendar en horarios disponibles.

Conceptos POO:

Clases: Medico, Paciente, Reserva, Horario.

Validar que no se crucen citas (comparación de fechas).

Guardar reservas en SQLite.

🔸 8. Sistema de Evaluaciones Académicas
Regla de negocio: Cada estudiante tiene calificaciones por materia y el promedio general define si aprueba o no.

Conceptos POO:

Clases: Estudiante, Materia, Nota.

Métodos: calcularPromedio(), esAprobado().

Uso de colecciones (List<Nota>) y control de estados.

🔸 9. Inventario con Alerta de Stock Bajo
Regla de negocio: El sistema debe alertar si un producto baja del mínimo permitido.

Conceptos POO:

Clase: Producto, Inventario.

Método: verificarStock().

Uso de HashMap<String, Integer> o List<Producto> con filtrado.

🔸 10. Conversor de Moneda usando API Simulada en JSON
Regla de negocio: El usuario debe poder convertir montos entre diferentes monedas según una tabla de cambio que se descarga desde un archivo JSON.

Conceptos POO:

Clase: ConversorMoneda, Moneda, TipoCambio.

Método: convertir("USD", "COP", monto)

Carga de tipos de cambio desde archivo JSON.
