#Enunciado: Crea un script en Python que, haga lo siguiente: 
#• Tome una palabra clave de búsqueda (puede ser una variable palabra = "laptop"). 
#• Ingrese a la tienda virtual (Puede ser Mercado libre o Amazon) 
#• Extraiga los títulos y precios de los primeros 5 productos que coincidan. 
#• Permite cambiar la palabra clave fácilmente. 
#Consideraciones: 
#• Solo impresión en consola. 
#• El script debe permitir cambiar fácilmente el término de búsqueda. 

import requests
from bs4 import BeautifulSoup
import time

def buscar_productos(palabra_clave):
    # Construir la URL con la palabra clave
    url = f"https://listado.mercadolibre.com.co/{palabra_clave}"
    
    # Realizar la solicitud HTTP
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        respuesta = requests.get(url, headers=headers)
        respuesta.raise_for_status()  # Verificar si la solicitud fue exitosa
        
        # Parsear el HTML
        soup = BeautifulSoup(respuesta.text, 'html.parser')
        
        # Encontrar los elementos que contienen productos
        productos = soup.find_all('div', class_='poly-card__content')
        
        # Imprimir los primeros 5 productos (o menos si hay menos resultados)
        print(f"\nResultados para: {palabra_clave}\n")
        
        contador = 0
        for producto in productos:
            if contador >= 5:
                break
                
            # Extraer el título
            titulo_elemento = producto.find('a', class_='poly-component__title')
            titulo = titulo_elemento.text.strip() if titulo_elemento else "Título no disponible"
            
            # Extraer el precio usando la estructura exacta proporcionada
            precio_div = producto.find('div', class_='poly-price__current')
            precio = "Precio no disponible"
            
            if precio_div:
                simbolo_elemento = precio_div.find('span', class_='andes-money-amount__currency-symbol')
                valor_elemento = precio_div.find('span', class_='andes-money-amount__fraction')
                
                if simbolo_elemento and valor_elemento:
                    simbolo = simbolo_elemento.text.strip()
                    valor = valor_elemento.text.strip()
                    precio = f"{simbolo}{valor}"
            
            # Imprimir la información
            print(f"Producto {contador + 1}:")
            print(f"Título: {titulo}")
            print(f"Precio: {precio}")
            print("-" * 50)
            
            contador += 1
            
        if contador == 0:
            print("No se encontraron productos con esa palabra clave.")
            
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

# Palabra clave inicial
palabra = "laptop"

# Buscar productos con la palabra clave inicial
print("Cargando resultados...")
buscar_productos(palabra)

# Permitir búsquedas continuas
while True:
    nueva_palabra = input("\nIngrese una nueva palabra clave para buscar (o presione Enter para salir): ")
    if not nueva_palabra:
        break
    
    print(f"Cargando resultados para '{nueva_palabra}'...")
    buscar_productos(nueva_palabra)

print("\nBúsqueda finalizada.")



