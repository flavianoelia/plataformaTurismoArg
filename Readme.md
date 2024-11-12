## Descripción del proyecto
En el presente trabajo se Desarrollar una plataforma de turismo nacional utilizando Django y aplicando los conceptos estudiados en la materia Programación 2: programación orientada a objetos, estructura de datos, árboles binarios, grafos y complejidad de algoritmos. Documentamos todas las fases del proyecto desde su concepción hasta la implementación final.
Objetivo general: Desarrollar una plataforma de turismo nacional que permita gestionar ciudades y rutas, ofreciendo rutas óptimas entre destinos.
Objetivos específicos:
Cargar ciudades con información turística relevante.
Implementar el algoritmo de Dijkstra para encontrar la ruta más corta entre ciudades.
Utilizar Árboles Binarios de Búsqueda (BST) para ordenar las ciudades antes de mostrar los datos en el frontend.

## Qué se hizo
Modelado y Estructura del Proyecto
Modelos: Describimos el modelo City y cómo se representa la información de cada ciudad.
El modelo consta de 3 atributos: nombre, descripción, población e imagen.
Árboles Binarios: Explicamos la implementación del Árbol Binario de Búsqueda (BST) y su utilidad en la organización de las ciudades a traves de los comentarios en el código.
Algoritmo de Dijkstra: Implementamos el algoritmo, cómo se calcula la ruta más corta y los resultados esperados con los comentarios en el código.
Frontend: Descripción de las modificaciones en los templates HTML proporcionados. 
Se modificó el archivo city_detail con los campos de las ciudades faltantes. Se creo la carpeta media en donde se ubican las imágenes de las ciudades, se agrego el archivo css y se indago sobre el manejo de los archivos static en Django, y además pusimos un logo representativo de la página el cual debió ser adaptado para aparecer en la pestaña de la página y en una dimensión más grande en cada una de las demás páginas. Todo esto teniendo en cuenta las modificaciones pertinentes para tratar archivos estáticos.
Añadimos los campos en el modelo cuidades y lo mostramos en el template. A través del Admin de Django cargamos las ciudades y las rutas.

Rutas de navegación: mostraremos un resumen de las URL configuradas.
Carga bidireccional de rutas (de ciudad1 a ciudad2 y viceversa).
Carga de imágenes de las ciudades y las mostramos en el detalle de cada ciudad.
Carga de fotos de las ciudades: implementamos el manejo de los archivos estáticos.
Implementación de Árboles Binarios de Búsqueda: Comentamos los métodos explicando su uso.
Algoritmo de Dijkstra: Implementamos desde cero para encontrar rutas óptimas. y comentamos el código.
Testing: implementamos tests para el método Dijkstra, las pruebas fueron satisfactorias.
 Manejo de errores: no nos aparecia la base de datos por lo que debimos buscar una extensión específica ya que no andaba la actual, también compartimos la base de datos individualmente para mantener la sincronización en el equipo, se resolvieron pequeños inconvenientes ligados a las políticas de privacidad para activar el entorno virtual pasando el siguiente comando: Set-ExecutionPolicy RemoteSigned - Scope Process.

## Análisis de complejidad del algoritmo de Dijkstra
En la inicialización, crea el diccionario, distances y previous_cities: O(1). Insertar el nodo en la cola de prioridad: O(log v). Bucle principal: extraer el nodo con la menor distancia de la cola de prioridad O(log v), para cada nodo recorrer sus vecinos (E veces en total): O(E). Actualizar la distancia y volver a insertar en la cola de prioridad: O(log v)
Notación Big-O
O ((V + E)\log V)
referencias:
(V) es el número de vertices (ciudades)
(E) es el número de aristas (rutas)

## Qué anda y qué no




## Qué se puede mejorar?