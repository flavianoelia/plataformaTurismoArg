# Plataforma de turismo Argentina

## Descripción del proyecto
En el presente trabajo se Desarrolla una plataforma de turismo nacional utilizando Django y aplicando los conceptos estudiados en la materia Programación 2: programación orientada a objetos, estructura de datos, árboles binarios, grafos y complejidad de algoritmos. Documentamos todas las fases del proyecto desde su concepción hasta la implementación final.
Objetivo general: Desarrollar una plataforma de turismo nacional que permita gestionar ciudades y rutas, ofreciendo rutas óptimas entre destinos.
Objetivos específicos:
Cargar ciudades con información turística relevante.
Implementar el algoritmo de Dijkstra para encontrar la ruta más corta entre ciudades.
Utilizar Árboles Binarios de Búsqueda (BST) para ordenar las ciudades antes de mostrar los datos en el frontend.

## ¿Qué se hizo?
Modelado y Estructura del Proyecto
Modelos: Describimos el modelo City y cómo se representa la información de cada ciudad.
El modelo consta de 4 atributos: nombre, descripción, población e imagen.
Árboles Binarios: Explicamos la implementación del Árbol Binario de Búsqueda (BST) y su utilidad en la organización de las ciudades a través de los comentarios en el código.
Algoritmo de Dijkstra: Implementamos el algoritmo, cómo se calcula la ruta más corta y los resultados esperados con los comentarios en el código.
Frontend: Descripción de las modificaciones en los templates HTML proporcionados. 
Se modificó el archivo city_detail con los campos de las ciudades faltantes. Se creo la carpeta media en donde se ubican las imágenes de las ciudades, se agrego el archivo css y se indago sobre el manejo de los archivos static en Django. Además pusimos un logo representativo de la página (con todo lo que la cuidad de Códoba tiene) el cual debió ser adaptado para aparecer en la pestaña de la página y en una dimensión más grande en cada una de las demás páginas. Todo esto teniendo en cuenta las modificaciones pertinentes para tratar archivos estáticos.
Añadimos los campos en el modelo cuidades y lo mostramos en el template. A través del Admin de Django cargamos las ciudades y las rutas.

Rutas de navegación: mostraremos un resumen de las URL configuradas.
Carga bidireccional de rutas (de ciudad1 a ciudad2 y viceversa).
Carga de imágenes de las ciudades y las mostramos en el detalle de cada ciudad. Implementamos el manejo de los archivos estáticos. Creamos la clase lugares turíticos para cada ciudad, agregando imanen y descripción a la de la ciudad de Córdoba.
Implementación de Árboles Binarios de Búsqueda: Comentamos los métodos explicando su uso.
Algoritmo de Dijkstra: Implementamos desde cero para encontrar rutas óptimas. y comentamos el código.
Testing: implementamos tests para el método Dijkstra. Especialmente testeamos que el algoritmo elija la ruta más corta sin pasar por Córdoba si hay una ruta directa, porque con los datos que en un principio había cargado, no obtenia el resultado esperado, luego de cargar rutas especificas y esperables los resultados de las pruebas fueron satisfactorias.
 Manejo de errores: no nos aparecia la base de datos por lo que debimos buscar una extensión específica ya que no andaba la actual, también compartimos la base de datos individualmente para mantener la sincronización en el equipo, se resolvieron pequeños inconvenientes ligados a las políticas de privacidad para activar el entorno virtual pasando el siguiente comando: Set-ExecutionPolicy RemoteSigned - Scope Process.

## Análisis de complejidad del algoritmo de Dijkstra
En la inicialización, crea el diccionario, distances y previous_cities: O(1). Insertar el nodo en la cola de prioridad: O(log v). Bucle principal: extraer el nodo con la menor distancia de la cola de prioridad O(log v), para cada nodo recorrer sus vecinos (E veces en total): O(E). Actualizar la distancia y volver a insertar en la cola de prioridad: O(log v)
Notación Big-O
O ((V + E)\log V)
referencias:
(V) es el número de vertices (ciudades)
(E) es el número de aristas (rutas)

## Qué anda y qué no?
### Anda:
- Algoritmo de Dijkstra
- Modelo de ciudades en el frontend
- Imagenes en la base de datos, como propiedad de las ciudades
- Test unitarios

## Qué se puede mejorar?
Se podría mejorar añadiendo una página de bienvenida para el usuario, inidicando de qué se trata la página y las secciones que tiene. También se podría estilizar más la página cambiando los colores, añadiendo animaciones y transiciones para que sea más agradable para el usuario, si bien no era parte de la consigna de trabajo, nos quedamos con muchas ganas de seguir trabajando en ella.

## Instrucciones de instalación

1. Clonar el repositorio:
    ```bash
    git clone https://github.com/flavianoelia/plataformaTurismoArg.git
    cd plataformaTurismoArg
    ```

2. Crear y activar un entorno virtual:
    ```bash
    python -m venv env
    source env/bin/activate  # En Windows: env\Scripts\activate
    ```

3. Instalar las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

4. Realizar las migraciones de la base de datos:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Crear un superusuario para acceder al administrador de Django:
    ```bash
    python manage.py createsuperuser
    ```

6. Ejecutar el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

7. Acceder al administrador de Django:
    - Abre tu navegador y ve a `http://127.0.0.1:8000/admin`
    - Inicia sesión con las credenciales del superusuario que creaste.

## Reproducción del entorno


Asegúrate de que la librería Pillow esté incluida en `requirements.txt`:

```plaintext
asgiref==3.8.1
Django==5.1.1
networkx==3.3
sqlparse==0.5.1
Pillow

### Agradecimientos

Quiero aprovechar este lugar, el mejor lugar, para expresar mi enorme agradecimiento a mi profesor Matías Eduardo Bordone, por todo lo que me ha enseñado y sobre todo por su forma de ser tan generosa de brindarlo todo, darnos más de lo que debía, por su gran vocación en la docencia. También quiero agradecerle a nuestro ayudante alumno Nicolás Dahlquist por su ayuda y predispoción no solo en este proyecto sino durante todo el año lectivo. Y a mi nuevo compañero de equipo Daniel LLanes, quien me ha hecho volver a creer en que sí se puede encontrar un buen equipo de trabajo.
