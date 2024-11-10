import heapq  # Importa heapq para gestionar la cola de prioridad.
from .models import City, Route  # Importa modelos relacionados con ciudades y rutas.

def dijkstra(start_city): #se le pasa una ciudad por parametro
    distances = {start_city: 0}  # diccionario que guarda las distancias y el nombre de la ciudad
    previous_cities = {start_city: None}  # Guarda las ciudades por las que se pasó para llegar
    priority_queue = [(0, start_city)] #cola de prioridad para recorrer el grafo
 
 # mientras haya nodos para recorrer en el grafo:
    while priority_queue:
        #extrae la menor distancia y la ciudad 
        current_distance, current_city = heapq.heappop(priority_queue) 

        #si la distancia actual es mayor a la d
        if current_distance > distances.get(current_city, float('inf')):
            continue

        # Recorre las rutas desde y hacia la ciudad actual (para un grafo no dirigido)
        for route in list(current_city.route_start.all()) + list(current_city.route_end.all()):
            # Verifica si la ciudad destino es el inicio o el fin de la ruta
            neighbor = route.end_city if route.start_city == current_city else route.start_city
            distance = current_distance + route.distance

        #verifica si la nueva distancia es menor a la ya registrada para ese vecino
            if distance < distances.get(neighbor, float('inf')):
                distances[neighbor] = distance #si es menor, la asigna como la nueva distancia
                previous_cities[neighbor] = current_city #actualiza la ciudad del vecino a la actual
                heapq.heappush(priority_queue, (distance, neighbor)) #agrega la distancia y el vecino a la cola de prioridad

    return distances, previous_cities

def get_shortest_path(start_city, end_city):
    """
    Devuelve el camino más corto entre dos ciudades usando el algoritmo de Dijkstra.
    - 'path': lista con las ciudades en el orden del camino más corto.
    - 'distances[end_city]': la distancia total mínima entre start_city y end_city.
    """
    distances, previous_cities = dijkstra(start_city) # Ejecuta el algoritmo Dijkstra.
    path = [] #Lista para almacenar el camino más corto en orden inverso
    city = end_city  # Comienza desde la ciudad destino.

#Reconstruir el camino desde el final al inicio
    while previous_cities[city] is not None: # agregue el is not None
        path.insert(0, city)# Inserta la ciudad al inicio de la lista
        city = previous_cities[city]
    path.insert(0, city)# Agrega la ciudad inicial

    return path, distances[end_city]

class ArbolBinarioBusqueda:
    """
    Implementa un Árbol Binario de Búsqueda (ABB), donde cada nodo tiene una clave única.
    Permite agregar, buscar y eliminar elementos de manera eficiente.
    """

    def __init__(self):
        """
        Inicializa el árbol vacío con su raíz en None y tamaño en 0.
        """
        self.raiz = None  # La raíz empieza vacía.
        self.tamano = 0  # El tamaño inicial es 0.

    def agregar(self,clave,valor):
        """
        Inserta un nodo con la clave y valor dados.
        Si la raíz ya existe, llama a _agregar para encontrar su posición.
        """
        if self.raiz:
            self._agregar(clave,valor,self.raiz) # Busca la posición adecuada.
        else:
            self.raiz = NodoArbol(clave,valor) # Define la raíz.
        self.tamano = self.tamano + 1  # Incrementa el tamaño.

    def _agregar(self,clave,valor,nodoActual):
        """
        Inserta recursivamente un nodo en el lugar adecuado del árbol.
        """
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                self._agregar(clave,valor,nodoActual.hijoIzquierdo)
            else:
                nodoActual.hijoIzquierdo = NodoArbol(clave,valor,padre=nodoActual)
        else:
            if nodoActual.tieneHijoDerecho():
                self._agregar(clave,valor,nodoActual.hijoDerecho)
            else:
                nodoActual.hijoDerecho = NodoArbol(clave,valor,padre=nodoActual)

    def __setitem__(self,c,v):
        self.agregar(c,v)

    def obtener(self,clave):
        """
        Devuelve el valor asociado a una clave específica. Si no se encuentra, retorna None.
        """
        if self.raiz:
            res = self._obtener(clave,self.raiz)
            if res:
                return res.cargaUtil
            else:
                return None
        else:
            return None

    def _obtener(self,clave,nodoActual):
        """
        Busca recursivamente el nodo con la clave dada.
        """
        if not nodoActual:
            return None
        elif nodoActual.clave == clave:
            return nodoActual
        elif clave < nodoActual.clave:
            return self._obtener(clave,nodoActual.hijoIzquierdo)
        else:
            return self._obtener(clave,nodoActual.hijoDerecho)
    
    def obtener_claves(self):
        """
        Devuelve una lista con todas las claves del árbol en orden ascendente.
        """
        claves = []
        self._obtener_claves(self.raiz, claves)
        return claves

    def _obtener_claves(self, nodoActual, claves):
        """
        Agrega recursivamente las claves en orden.
        """
        if nodoActual:
            self._obtener_claves(nodoActual.hijoIzquierdo, claves)  # Recorrer el hijo izquierdo
            claves.append(nodoActual.clave)  # Añadir la clave del nodo actual
            self._obtener_claves(nodoActual.hijoDerecho, claves)  # Recorrer el hijo derecho

    def obtener_lista(self):
        """Devuelve una lista con los valores de todos los nodos en orden ascendente."""
        return [self.obtener(clave) for clave in self.obtener_claves()]
        # Utiliza una lista por comprensión para obtener los valores de cada clave en el árbol.

    def __getitem__(self,clave):
        """
    Permite acceder al valor asociado a una clave como si se tratara de un diccionario.
    Si la clave no existe, lanza una excepción KeyError.
    """
        res = self.obtener(clave)
        if res:
            return res
        else:
            raise KeyError('Error, la clave no está en el árbol')

    def __contains__(self,clave):
        """
    Permite verificar si una clave está en el árbol con la sintaxis 'clave in arbol'.
    Devuelve True si la clave está presente, de lo contrario False.
    """
        if self._obtener(clave,self.raiz):
            return True
        else:
            return False

    def longitud(self):
        """Devuelve el número total de nodos en el árbol."""
        return self.tamano

    def __len__(self):
        """
        Permite obtener la cantidad de nodos con la función 'len()'.
        Es equivalente al método longitud().
        """
        return self.tamano

    def __iter__(self):
        """
        Permite iterar sobre los nodos del árbol.
        Asume que la clase NodoArbol implementa su propio método __iter__.
        """
        return self.raiz.__iter__()

    def eliminar(self,clave):
        """
        Elimina el nodo con la clave dada, ajustando los nodos hijos si es necesario.
        """
        if self.tamano > 1:
            nodoAEliminar = self._obtener(clave,self.raiz)
            if nodoAEliminar:
                self.remover(nodoAEliminar)
                self.tamano = self.tamano-1
            else:
                raise KeyError('Error, la clave no está en el árbol')
        elif self.tamano == 1 and self.raiz.clave == clave:
            self.raiz = None
            self.tamano = self.tamano - 1
        else:
            raise KeyError('Error, la clave no está en el árbol')

    def __delitem__(self,clave):
        """
    Sobrecarga el operador 'del' para permitir la eliminación de un nodo 
    del árbol binario de búsqueda usando la clave especificada.
    """
        self.eliminar(clave)  # Llama al método 'eliminar' para remover el nodo correspondiente.

    def remover(self,nodoActual):
        """
        Remueve un nodo del árbol, ajustando sus hijos si es necesario.
        """
        if nodoActual.esHoja(): #Caso 1: El nodo es hoja
            if nodoActual == nodoActual.padre.hijoIzquierdo:
                nodoActual.padre.hijoIzquierdo = None
            else:
                nodoActual.padre.hijoDerecho = None
        elif nodoActual.tieneAmbosHijos():  # Caso 2: Tiene dos hijos.(interior)
            suc = nodoActual.encontrarSucesor()
            suc.empalmar()
            nodoActual.clave = suc.clave
            nodoActual.cargaUtil = suc.cargaUtil

        else: # Caso 3: este nodo tiene un (1) solo hijo
            if nodoActual.tieneHijoIzquierdo():
                if nodoActual.esHijoIzquierdo():
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoIzquierdo
                elif nodoActual.esHijoDerecho():
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre
                    nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo
                else:
                    nodoActual.reemplazarDatoDeNodo(nodoActual.hijoIzquierdo.clave, nodoActual.hijoIzquierdo.cargaUtil, nodoActual.hijoIzquierdo.hijoIzquierdo, nodoActual.hijoIzquierdo.hijoDerecho)
            else:
                if nodoActual.esHijoIzquierdo():
                    nodoActual.hijoDerecho.padre = nodoActual.padre
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoDerecho
                elif nodoActual.esHijoDerecho():
                    nodoActual.hijoDerecho.padre = nodoActual.padre
                    nodoActual.padre.hijoDerecho = nodoActual.hijoDerecho
                else:
                    nodoActual.reemplazarDatoDeNodo(nodoActual.hijoDerecho.clave, nodoActual.hijoDerecho.cargaUtil, nodoActual.hijoDerecho.hijoIzquierdo, nodoActual.hijoDerecho.hijoDerecho)

    def inorden(self):
        """Recorre el árbol en orden.
        Primero recorre el subárbol izquierdo, 
        luego visita el nodo actual 
        y finalmente recorre el subárbol derecho"""
        self._inorden(self.raiz)

    def _inorden(self,arbol):
        if arbol != None:
            self._inorden(arbol.hijoIzquierdo)
            print(arbol.clave)
            self._inorden(arbol.hijoDerecho)

    def postorden(self):
        """Recorre el árbol en postorden.
        Primero recorre el subárbol izquierdo,
        luego recorre el subárbol derecho 
        y finalmente visita el nodo actual"""
        self._postorden(self.raiz)

    def _postorden(self, arbol):
        if arbol:
            self._postorden(arbol.hijoIzquierdo)
            self._postorden(arbol.hijoDerecho)
            print(arbol.clave)

    def preorden(self):
        """Recorre el árbol en preorden.
        Primero visita el nodo actual,
        luego recorre el subárbol izquierdo
        y finalmente el subárbol derecho"""
        self._preorden(self.raiz) 

    def _preorden(self,arbol):
        if arbol:
            print(arbol.clave)
            self._preorden(arbol.hijoIzquierdo)
            self._preorden(arbol.hijoDerecho)

class NodoArbol:
    """
    Representa un nodo en el árbol binario de búsqueda con claves y valores.
    """
    def __init__(self,clave,valor,izquierdo=None,derecho=None,padre=None):
        """
        Inicializa un nodo con clave, valor, y referencias a sus hijos y su padre.
        """
        self.clave = clave  # Asignación de la clave del nodo para realizar comparaciones
        self.cargaUtil = valor  # Valor asociado a la clave (puede ser cualquier tipo de dato)
        # Referencias a los hijos izquierdo y derecho (inicialmente None)
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre # Referencia al nodo padre (útil para seguir el camino hacia arriba)
        self.factorEquilibrio = 0 # Factor de equilibrio (usado en árboles balanceados como AVL)

    def tieneHijoIzquierdo(self):
        """Devuelve True si el nodo tiene un hijo izquierdo."""
        return self.hijoIzquierdo

    def tieneHijoDerecho(self):
        """Devuelve True si el nodo tiene un hijo derecho."""
        return self.hijoDerecho

    def esHijoIzquierdo(self):
        """
        Verifica si este nodo es el hijo izquierdo de su padre.
        """
        return self.padre and self.padre.hijoIzquierdo == self

    def esHijoDerecho(self):
        """
        Verifica si este nodo es el hijo derecho de su padre.
        """
        return self.padre and self.padre.hijoDerecho == self

    def esRaiz(self):
        """Devuelve True si el nodo es la raíz del árbol."""
        return not self.padre

    def esHoja(self):
        """Devuelve True si el nodo no tiene hijos."""
        return not (self.hijoDerecho or self.hijoIzquierdo)

    def tieneAlgunHijo(self):
        """Devuelve True si el nodo tiene al menos un hijo."""
        return self.hijoDerecho or self.hijoIzquierdo

    def tieneAmbosHijos(self):
        """Devuelve True si el nodo tiene tanto hijo izquierdo como derecho."""
        return self.hijoDerecho and self.hijoIzquierdo

    def reemplazarDatoDeNodo(self,clave,valor,hizq,hder):
        """
        Reemplaza los datos del nodo actual y actualiza las referencias
        de los hijos si es necesario.
        """
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
         # Actualiza la referencia al padre en los hijos
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self

    def encontrarSucesor(self):
        """
        Encuentra el sucesor del nodo (el siguiente nodo más grande).
        """
        suc = None
        if self.tieneHijoDerecho():
            # El sucesor es el nodo mínimo del subárbol derecho
            suc = self.hijoDerecho.encontrarMin()
        else:
            if self.padre:
                if self.esHijoIzquierdo():
                    # Si es hijo izquierdo, el sucesor es su padre
                    suc = self.padre
                else:
                    # Caso en que es hijo derecho: buscar hacia arriba
                    self.padre.hijoDerecho = None
                    suc = self.padre.encontrarSucesor()
                    self.padre.hijoDerecho = self
        return suc

    def empalmar(self):
        """
        Elimina el nodo actual ajustando las referencias entre su padre
        y sus hijos para mantener la estructura del árbol.
        """
        if self.esHoja():
            # Si es una hoja, simplemente se elimina del árbol
            if self.esHijoIzquierdo():
                self.padre.hijoIzquierdo = None
            else:
                self.padre.hijoDerecho = None
        elif self.tieneAlgunHijo():
            # Si tiene un hijo, reemplaza el nodo por su hijo
            if self.tieneHijoIzquierdo():
                if self.esHijoIzquierdo():
                    self.padre.hijoIzquierdo = self.hijoIzquierdo
                else:
                    self.padre.hijoDerecho = self.hijoIzquierdo
                self.hijoIzquierdo.padre = self.padre
            else:
                if self.esHijoIzquierdo():
                    self.padre.hijoIzquierdo = self.hijoDerecho
                else:
                    self.padre.hijoDerecho = self.hijoDerecho
                self.hijoDerecho.padre = self.padre

    def encontrarMin(self):
        """
        Encuentra el nodo con la clave mínima en el subárbol.
        """
        actual = self
        # Recorrer hacia abajo hasta encontrar el nodo más a la izquierda
        while actual.tieneHijoIzquierdo():
            actual = actual.hijoIzquierdo
        return actual

    def __iter__(self):
        """
        Implementa el iterador para recorrer el árbol en orden ascendente.
        """
        if self:
            if self.tieneHijoIzquierdo():
                 # Recorre el subárbol izquierdo primero
                for elem in self.hijoIzquierdo:
                    yield elem
            # Devuelve la clave del nodo actual
            yield self.clave
            if self.tieneHijoDerecho():
                # Luego recorre el subárbol derecho
                for elem in self.hijoDerecho:
                    yield elem