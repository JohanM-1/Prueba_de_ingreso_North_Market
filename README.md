# Prueba Técnica North Market

## Descripción
Este repositorio contiene la solución a tres pruebas técnicas para North Market:

1. **Ejercicio de Algoritmos**: Función para encontrar el número más frecuente en una lista.
2. **Web Scraping**: Script para extraer información de productos de Mercado Libre.
3. **Aplicación con Interfaz Gráfica y API**: Sistema de login con base de datos SQLite que muestra información de la API de Rick and Morty.

## Requisitos de Instalación

Para ejecutar las pruebas, necesitarás Python 3.6 o superior y las siguientes librerías:

```bash
# Instalar dependencias
pip install requests beautifulsoup4 tkinter
```

En Windows, tkinter generalmente viene incluido con la instalación de Python.

## Pruebas Resueltas

### Prueba 1: Función para encontrar número más frecuente
- Archivo: `#1.py`
- No requiere librerías adicionales
- Ejecutar: `python "#1.py"`

### Prueba 2: Web Scraping de Mercado Libre
- Archivo: `#2.py`
- Librerías: requests, BeautifulSoup
- Ejecutar: `python "#2.py"`
- Permite buscar productos por palabra clave y muestra título y precio de los primeros 5 resultados

### Prueba 3: Sistema de Login con API
- Archivo: `#3.py`
- Librerías: tkinter, sqlite3, requests
- Ejecutar: `python "#3.py"`
- Credenciales de prueba:
  - Usuario: admin / Contraseña: admin123
  - Usuario: usuario / Contraseña: password
  - Usuario: test / Contraseña: test123
- Al iniciar sesión correctamente, muestra datos de personajes de la API de Rick and Morty

## Base de datos
- La aplicación utiliza una base de datos SQLite (`users.db`) que se crea automáticamente si no existe.
- Contiene una tabla `usuarios` con campos `username` y `password`.
