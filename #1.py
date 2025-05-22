#Enunciado: Crea una función llamada numero_mas_frecuente(lista) que reciba una lista de 
#números enteros y devuelva el número que más veces se repite. Si hay más de uno con la 
#misma frecuencia, devuelve el menor de ellos. 
#Ejemplo: 
#numero_mas_frecuente([1, 3, 1, 3, 2, 1]) 
# Resultado esperado: 1 
#numero_mas_frecuente([4, 4, 5, 5])       
#Resultado esperado: 4 

def numero_mas_frecuente(lista):
    frecuencia = {}
    max_frecuencia = 0
    result = None

    for numero in lista:
        frecuencia[numero] = frecuencia.get(numero, 0) + 1
        
        if frecuencia[numero] > max_frecuencia:
            max_frecuencia = frecuencia[numero]
            result = numero
            
        elif frecuencia[numero] == max_frecuencia and (result is None or numero < result):
            result = numero

    return result

    
    

print(numero_mas_frecuente([1, 3, 1, 3, 2, 1]))
print(numero_mas_frecuente([4, 4, 5, 5]))
