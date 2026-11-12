# Fundamentos de Internet 

## 1. Del Cliente al Servidor
1. Tu navegador (Cliente) pide ayuda. Escribes "www.youtube.com" y das Enter. Tu navegador sabe el nombre de la página, pero no sabe dónde está alojada físicamente porque las computadoras solo se entienden con números (direcciones IP).
2. El DNS busca la dirección. Como tu navegador no se sabe el número, le pregunta al DNS, que funciona como la agenda de contactos de internet. El DNS busca "www.youtube.com" y le devuelve su dirección IP (por ejemplo, 142.250.190.46).
3. La dirección IP marca el camino. Con esa IP, que es como la dirección postal exacta de YouTube en el mundo, tu navegador ya sabe exactamente a dónde enviar la señal a través de internet.
4. HTTPS asegura la videollamada. Antes de pedir el video, el navegador y YouTube usan el protocolo HTTPS para crear una conexión segura y secreta (un "apretón de manos" digital). Así, nadie puede espiar lo que estás viendo. Luego, el navegador le dice: "Hola, quiero ver este video".
5. El Servidor de YouTube responde El servidor (la gran computadora de YouTube) recibe el mensaje, busca el archivo del video en sus discos duros y se lo empieza a mandar a tu navegador en pedacitos digitales.
6. El video aparece en tu pantalla Tu navegador recibe esos pedacitos, los junta en milisegundos como un rompecabezas y ¡listo!, el video empieza a reproducirse en tu pantalla.

[ Tu Navegador ] -------- 1. ¿Cuál es el número de YouTube? -------> [ Agenda DNS ]
[   (Cliente)  ] <------- 2. Su dirección IP es: 142.250... <------- [ (Directorio) ]
       |
       | 3. Usa la IP para llegar.
       | 4. Conecta de forma segura (HTTPS) y pide el video.
       v
[ Servidor YouTube ] ---- 5. Procesa y envía los pedacitos del video -> [ Tu Pantalla ]

## 2. Frontend y Backend en acción
División del Sistema:
El Frontend es la cara visible de la aplicación, es decir, todo lo que el paciente ve y toca en su pantalla para elegir el médico, la fecha y la hora.
El Backend es el cerebro oculto en el servidor, el cual verifica que el médico esté disponible, guarda la cita en la base de datos y envía el correo de confirmación.

Tecnologías recomendadas:
Para el Frontend: React, Vue.js o HTML/CSS/JavaScript nativo.
Para el Backend: Node.js (con Express), Python (con FastAPI o Django) o PHP.

¿Cómo se comunican?
Cuando el paciente hace clic en "Agendar Cita", el Frontend crea un mensaje digital llamado Request (Petición) que viaja a través del protocolo HTTP (el canal de comunicación de internet).
Esta petición viaja hacia una API, que funciona como una ventanilla de atención en el Backend encargada de recibir los datos de la cita. El Backend procesa la información, la guarda y le devuelve al Frontend una Response (Respuesta) confirmando que la cita fue exitosa para que la pantalla le muestre un mensaje verde al usuario.

## 3. REST vs SOAP vs GraphQL

| Tipo de API | Formato de datos usado | Nivel de flexibilidad | Dificultad de implementación | Uso actual (Alta / Media / Baja) |
| **REST**    | Principalmente **JSON** (también XML, HTML, texto) | **Media** (Estructura fija por endpoint) | **Baja** (Muy intuitivo, basado en HTTP) | **Alta** (Estándar de la web a ctual) |
| **SOAP** | Estrictamente **XML** | **Baja** (Contratos rígidos con WSDL) | **Alta** (Configuraciones complejas) | **Media / Baja** (Sistemas bancarios y heredados) |
| **GraphQL** | Estrictamente **JSON** | **Alta** (El cliente pide solo lo que necesita) | **Media** (Requiere configurar esquemas) | **Alta / Media** (Gran crecimiento en apps móviles/web) |

** ¿Cuál es más apropiada para una startup moderna? ¿Por qué? **

Razones por las que REST es la mejor opción para la startup: 

* Velocidad de lanzamiento: Permite desarrollar el prototipo inicial mucho más rápido debido a su baja dificultad y abundancia de herramientas listas para usar. 
* Ecosistema y talento: Es el estándar absoluto de la industria; es extremadamente fácil contratar programadores que ya sepan REST y conectarlo con pasarelas de pago (como Stripe) o servicios de mapas que usan este mismo estándar. 
* Facilidad de mantenimiento: Un sistema de reservas en línea no tiene una complejidad de datos tan extrema al inicio que justifique la infraestructura de GraphQL, manteniendo el código simple y fácil de corregir durante el crecimiento de la empresa. 


## 4. Explorando APIs con Postman

### 4.1 Selección de la API


- ** Nombre de la API: **
    https://jsonplaceholder.typicode.com/

- ** Descripción: **
    JSONPlaceholder es una API REST falsa y gratuita en línea que se utiliza para realizar pruebas y prototipos de software. Está activa desde 2013 y procesa miles de millones de solicitudes al mes, ofreciendo datos ficticios en formato JSON de forma inmediata sin necesidad de registrarse ni usar claves de API


### 4.2 Configuración en Postman

- ** Nombre de la colección: **
    JSONplaceholder

- ** Solicitudes agregadas: **

- GET -
    https://jsonplaceholder.typicode.com/posts/1

  
- POST -
    https://jsonplaceholder.typicode.com/posts

  
- PUT/PATCH/DELETE -
    https://jsonplaceholder.typicode.com/posts/101

### 4.3 Ejecución y análisis

| Solicitud         | Método        | Endpoint  | Código de estado | Notas |
| :--- | :--- | :--- | :--- | :--- |
| **Obtener publicación** | `GET` | `/posts/1` | `200 OK` | Devuelve el objeto del post con `id: 1` en formato JSON. |
| **Crear publicación** | `POST` | `/posts` | `201 Created` | Simula la creación del recurso y retorna el objeto con un `id: 101` asignado. |
| **Actualizar por completo** | `PUT` | `/posts/101` | `200 OK` / `201 Created` | Reemplaza o simula la actualización completa del recurso `101`. |
| **Actualizar parcialmente** | `PATCH` | `/posts/101` | `200 OK` | Modifica únicamente los campos enviados en el cuerpo del request. |
| **Eliminar publicación** | `DELETE` | `/posts/101` | `200 OK` | Simula el borrado del recurso en el servidor devolviendo un objeto vacío `{}`. |





### 4.4 Explicación técnica

#### Obtener publicación

- **Método HTTP:** `GET`

- **Endpoint:** `/posts/1`

- **Parámetros / body:** Ninguno (parámetro de ruta `id: 1`).

- **Descripción de la respuesta:** Retorna un objeto JSON con la información detallada de la publicación solicitada, que incluye los campos `userId`, `id`, `title` y `body`.

---

#### Crear publicación

- **Método HTTP:** `POST`

- **Endpoint:** `/posts`

- **Parámetros / body:** Requiere un objeto JSON en el cuerpo del request con las propiedades deseadas (por ejemplo: `title`, `body` y `userId`) y el header `Content-type: application/json; charset=UTF-8`.

- **Descripción de la respuesta:** Retorna el objeto simulado como si hubiera sido creado con éxito, asignándole un nuevo identificador (`id: 101`) junto a las propiedades enviadas.

---

#### Actualizar publicación (Completa)

- **Método HTTP:** `PUT`

- **Endpoint:** `/posts/101`

- **Parámetros / body:** Requiere el objeto JSON completo en el cuerpo con las propiedades actualizadas y el campo `id`.

- **Descripción de la respuesta:** Retorna el recurso completo simulando la actualización en el servidor.

---

#### Actualizar publicación (Parcial)

- **Método HTTP:** `PATCH`

- **Endpoint:** `/posts/101`

- **Parámetros / body:** Requiere un objeto JSON que contenga únicamente los atributos específicos que se desean modificar (por ejemplo, solo el `title`).

- **Descripción de la respuesta:** Retorna el recurso modificado con los campos nuevos aplicados y el resto de la estructura original intacta.

---

#### Eliminar publicación

- **Método HTTP:** `DELETE`

- **Endpoint:** `/posts/101`

- **Parámetros / body:** Ninguno.

- **Descripción de la respuesta:** Devuelve una confirmación de éxito con un objeto JSON vacío `{}` para indicar que el recurso ha sido simulado como borrado.

---

**¿Qué aprendiste del proceso?**

1. **Simulación del lado del servidor (Faking):** JSONPlaceholder no persiste los cambios reales en su base de datos al usar métodos de escritura (`POST`, `PUT`, `PATCH`, `DELETE`). Las respuestas exitosas son simulaciones directas (`faked as if`) para que el cliente pueda evaluar la estructura de retorno en el desarrollo del software.
2. **Diferencia entre PUT y PATCH:** Mientras que `PUT` reemplaza completamente el objeto en la ruta designada, `PATCH` modifica de manera quirúrgica solo los fragmentos o propiedades enviados por el cliente.
3. **Consistencia de las APIs REST:** El diseño basado en estándares HTTP puros (`GET` para leer, `POST` para crear, etc.) y tipos de contenido claros como `application/json` garantiza que las herramientas de testing y el software sigan siendo compatibles a lo largo del tiempo.
