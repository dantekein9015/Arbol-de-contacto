# Trabajo práctico - Árbol de contactos en Python
#Github:https://github.com/dantekein9015/Arbol-de-contacto

import time

# Clase que representa un contacto
class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre} - {self.telefono}"

# Nodo del árbol binario
class Nodo:
    def __init__(self, contacto):
        self.contacto = contacto
        self.izquierda = None
        self.derecha = None

# Árbol binario de contactos
class ArbolContactos:
    def __init__(self):
        self.raiz = None

    def insertar(self, contacto):
        def _insertar(nodo, contacto):
            if nodo is None:
                return Nodo(contacto)
            if contacto.nombre < nodo.contacto.nombre:
                nodo.izquierda = _insertar(nodo.izquierda, contacto)
            else:
                nodo.derecha = _insertar(nodo.derecha, contacto)
            return nodo

        self.raiz = _insertar(self.raiz, contacto)

    def buscar(self, nombre):
        def _buscar(nodo, nombre):
            if nodo is None:
                return None
            if nombre == nodo.contacto.nombre:
                return nodo.contacto
            elif nombre < nodo.contacto.nombre:
                return _buscar(nodo.izquierda, nombre)
            else:
                return _buscar(nodo.derecha, nombre)

        return _buscar(self.raiz, nombre)

    def inorden(self):
        resultados = []

        def _inorden(nodo):
            if nodo:
                _inorden(nodo.izquierda)
                resultados.append(str(nodo.contacto))
                _inorden(nodo.derecha)

        _inorden(self.raiz)
        return resultados

# --- PRUEBA / MENÚ INTERACTIVO ---

def main():
    arbol = ArbolContactos()
    nombres = ["Carlos", "Ana", "Diego", "Romina", "Enrique", "Juan", "Gabriela", "Hector"]

    print("Insertando contactos...")

    inicio_insercion = time.time()
    for i, nombre in enumerate(nombres):
        telefono = f"+54 9 11 0000-{i:04}"
        arbol.insertar(Contacto(nombre, telefono))
    fin_insercion = time.time()

    print("Contactos insertados correctamente.")
    print(f"Tiempo total de inserción: {fin_insercion - inicio_insercion:.6f} segundos\n")

    while True:
        print("\n--- MENÚ ---")
        print("1. Buscar contacto")
        print("2. Ver todos los contactos (orden alfabético)")
        print("3. Agregar nuevo contacto")
        print("4. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            nombre = input("Nombre a buscar: ")
            inicio_busqueda = time.time()
            contacto = arbol.buscar(nombre)
            fin_busqueda = time.time()
            if contacto:
                print(f"📇 Contacto encontrado: {contacto}")
            else:
                print("❌ Contacto no encontrado.")
            print(f"Tiempo de búsqueda: {fin_busqueda - inicio_busqueda:.6f} segundos")

        elif opcion == "2":
            print("\n📚 Contactos ordenados alfabéticamente:")
            for c in arbol.inorden():
                print(c)

        elif opcion == "3":
            nombre = input("Nombre del nuevo contacto: ")
            telefono = input("Teléfono: ")
            arbol.insertar(Contacto(nombre, telefono))
            print("✅ Contacto agregado.")

        elif opcion == "4":
            print("¡Hasta la próxima!")
            break
        else:
            print("❗ Opción no válida.")

if __name__ == "__main__":
    main()
