import heapq

def mezcla_directa(nombre, B):
    """Aplica el algoritmo de mezcla directa a un archivo de texto.

    Este algoritmo divide el contenido del archivo en bloques, ordena
    cada bloque y luego fusiona los bloques ordenados para obtener un
    archivo ordenado final.

    Args:
     nombre (str): El nombre del archivo de entrada.
     B (int): El tamaño de los bloques utilizados en la ordenación.

    """

    archivo_ordenado = 'ordenado.txt'
    bloques = dividir_archivo(nombre, B)

    for bloque in bloques:
        bloque.sort(key=lambda linea: obtener_numero_entero(linea))

    with open(archivo_ordenado, 'w') as ordenado:
        merged = merge_blocks(bloques)
        for linea in merged:
            ordenado.write(linea)

def dividir_archivo(nombre, B):
    """Divide un archivo en bloques de tamaño B.

    Args:
        nombre (str): El nombre del archivo de entrada.
        B (int): El tamaño de los bloques.

    Returns:
        list: Una lista de bloques, donde cada bloque es una lista de líneas.

    """
    bloques = []
    bloque_actual = []
    with open(nombre, 'r') as archivo:
        for linea in archivo:
            bloque_actual.append(linea)
            if len(bloque_actual) == B:
                bloques.append(bloque_actual.copy())
                bloque_actual.clear()

    if len(bloque_actual) > 0:
        bloques.append(bloque_actual.copy())

    return bloques

def obtener_numero_entero(linea):
    """Obtiene el primer número entero de una línea de texto.

    Args:
        linea (str): La línea de texto en la que se buscará el número entero.

    Returns:
        int: El número entero encontrado en la línea o 0 si no se encuentra ninguno.

    """
    palabras = linea.strip().split()
    for palabra in palabras:
        try:
            numero_entero = int(palabra.strip())
            return numero_entero
        except ValueError:
            continue

    return 0

def merge_blocks(bloques):
    """Fusiona bloques ordenados en un solo bloque ordenado.

    Args:
        bloques (list): Una lista de bloques, donde cada bloque es una lista de líneas ordenadas.

    Returns:
        list: Una lista de líneas que representa el bloque fusionado y ordenado.

    """
    heap = []
    merged = []
    for bloque in bloques:
        linea = bloque.pop(0)
        if linea:
            heap.append((obtener_numero_entero(linea), linea, bloque))

    heapq.heapify(heap)
    while heap:
        _, linea, bloque = heapq.heappop(heap)
        merged.append(linea)

        if bloque:
            linea = bloque.pop(0)
            heapq.heappush(heap, (obtener_numero_entero(linea), linea, bloque))

    return merged

# Aplicar el algoritmo de mezcla directa al archivo generado previamente
mezcla_directa('datos.txt', 10000)
print ("ordenado!")