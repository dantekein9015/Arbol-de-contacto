# 📚 Árbol Binario de Búsqueda en Python – Agenda de Contactos

Este proyecto implementa una **agenda de contactos** utilizando un **árbol binario de búsqueda (ABB)** en Python.  
Es un trabajo práctico integrador para la materia **Programación I** de la Tecnicatura Universitaria en Programación.

---

## 📌 Funcionalidades

- ✅ Insertar contactos con nombre y teléfono.
- 🔍 Buscar contactos por nombre (orden alfabético).
- 📄 Imprimir todos los contactos ordenados alfabéticamente.
- ⏱️ Medir tiempos de inserción y búsqueda usando `time`.

---

## 🧱 Estructura del código

### `class Contacto`
Representa un contacto individual con nombre y teléfono.

### `class Nodo`
Cada nodo del árbol contiene un objeto `Contacto` y enlaces a su subárbol izquierdo y derecho.

### `class ArbolContactos`
Maneja toda la lógica del árbol:
- `insertar()`: inserta contactos.
- `buscar()`: busca por nombre.
- `inorden()`: devuelve lista ordenada.

---

## ▶️ Ejecución

1. Cloná el repositorio:
```bash
git clone https://github.com/tuusuario/arbol-contactos.git
cd arbol-contactos
```

2. Ejecutá el programa:
```bash
python arbol_contactos.py
```

---

## 🧪 Ejemplo de salida

```
Contactos ordenados alfabéticamente:
Ana
Carlos
Diego
Gabriela
Hector

Resultado de búsqueda:
Gabriela - +54 9 11 0000-0006

Tiempo total de inserción: 0.000012 segundos
Tiempo de búsqueda: 0.000003 segundos
```

---

## 🛠️ Requisitos

- Python 3.6 o superior
- Editor recomendado: Visual Studio Code

---

## 📖 Aprendizajes

Este proyecto permite ejercitar:
- Uso de clases y objetos
- Recursividad
- Estructuras dinámicas (árboles)
- Medición de rendimiento básico

---

## 👥 Autores

- Juan Martín Figuerero Amicone  
- Enrique Alejandro Juarez Alvarez  

Facultad: *Tecnicatura Universitaria en Programación UTN*  
Año: 2025

