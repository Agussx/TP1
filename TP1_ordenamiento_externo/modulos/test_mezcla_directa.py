import os

def verificar_ordenamiento(archivo_original, archivo_ordenado):
    # Verificar el tamaño del archivo
    tam_original = os.path.getsize(archivo_original)
    tam_ordenado = os.path.getsize(archivo_ordenado)
    
    if tam_original == tam_ordenado:
        print("El tamaño del archivo es correcto.")
    else:
        print("Error: El tamaño del archivo no coincide.")
        return
    
    # Verificar el ordenamiento de los datos
    with open(archivo_ordenado, 'r') as archivo:
        lineas_ordenadas = archivo.readlines()
    
    for i in range(len(lineas_ordenadas) - 1):
        numero_actual = obtener_numero_entero(lineas_ordenadas[i])
        numero_siguiente = obtener_numero_entero(lineas_ordenadas[i+1])
        
        if numero_actual > numero_siguiente:
            print("Error: El archivo no está ordenado correctamente.")
            return
    
    print("El archivo está ordenado correctamente.")

def obtener_numero_entero(linea):
    palabras = linea.strip().split()
    for palabra in palabras:
        try:
            numero_entero = int(palabra.strip())
            return numero_entero
        except ValueError:
            continue

    return 0



# Ejecutar la función de verificación
verificar_ordenamiento('datos.txt', 'ordenado.txt')