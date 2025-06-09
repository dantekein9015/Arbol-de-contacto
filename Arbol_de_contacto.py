# Trabajo práctico - Árbol de contactos en Python

import time

# Clase que representa un contacto con nombre y teléfono
class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre} - {self.telefono}"

# Cada nodo del árbol guarda un contacto
class Nodo:
    def __init__(self, contacto):
        self.contacto = contacto
        self.izquierda = None  # hijo menor (alfabéticamente)
        self.derecha = None    # hijo mayor

# Acá está el árbol en sí, donde insertamos y buscamos contactos
class ArbolContactos:
    def __init__(self):
        self.raiz = None

    # Insertamos un contacto en el lugar correcto del árbol
    def insertar(self, contacto):
        def _insertar(nodo, contacto):
            if not nodo:
                return Nodo(contacto)
            if contacto.nombre < nodo.contacto.nombre:
                nodo.izquierda = _insertar(nodo.izquierda, contacto)
            else:
                nodo.derecha = _insertar(nodo.derecha, contacto)
            return nodo

        self.raiz = _insertar(self.raiz, contacto)

    # Buscamos un contacto por nombre
    def buscar(self, nombre):
        def _buscar(nodo, nombre):
            if not nodo:
                return None  # no lo encontró
            if nombre == nodo.contacto.nombre:
                return nodo.contacto
            elif nombre < nodo.contacto.nombre:
                return _buscar(nodo.izquierda, nombre)
            else:
                return _buscar(nodo.derecha, nombre)

        return _buscar(self.raiz, nombre)

    # Recorremos el árbol de forma ordenada (alfabéticamente)
    def inorden(self):
        resultados = []

        def _inorden(nodo):
            if nodo:
                _inorden(nodo.izquierda)
                resultados.append(str(nodo.contacto))
                _inorden(nodo.derecha)

        _inorden(self.raiz)
        return resultados

# --- PRUEBA DEL PROGRAMA ---

# Lista de nombres de prueba (amigos, familia, etc.)
nombres = ["Carlos", "Ana", "Diego", "Romina", "Enrique", "Juan", "Gabriela", "Hector"]

# Creamos el árbol vacío
arbol = ArbolContactos()

# Medimos cuánto tarda en insertar todos los contactos
inicio_insercion = time.time()
for nombre in nombres:
    telefono = f"+54 9 11 0000-{nombres.index(nombre):04}"  # número de contacto
    arbol.insertar(Contacto(nombre, telefono))
fin_insercion = time.time()

# Ahora medimos cuánto tarda en buscar un contacto puntual
inicio_busqueda = time.time()
resultado = arbol.buscar("Hector")
fin_busqueda = time.time()

# Mostramos los contactos ordenados
print("Contactos ordenados alfabéticamente:")
for contacto in arbol.inorden():
    print(contacto)

# Mostramos el resultado de la búsqueda
print("\nResultado de búsqueda:")
print(resultado)

# Mostramos los tiempos
print(f"\nTiempo total de inserción: {fin_insercion - inicio_insercion:.6f} segundos")
print(f"Tiempo de búsqueda: {fin_busqueda - inicio_busqueda:.6f} segundos")
