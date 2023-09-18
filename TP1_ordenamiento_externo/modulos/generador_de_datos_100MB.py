from random import randint, uniform
import os
import random

def crear_archivo_de_datos(nombre):
    """Crea un archivo de datos aleatorios con números enteros y flotantes.

    Este código genera un archivo de datos con una cantidad específica de valores
    aleatorios, donde cada valor es un número entero seguido de un conjunto de
    números flotantes con una cantidad fija de dígitos después del punto decimal.

    Args:
        nombre (str): El nombre del archivo de datos a crear.

    """
    f = 10**6
    N = 50 * f * 2
    cifras_entero = 6  # Reducimos la cantidad de dígitos en el número entero, para leer mejor
    tam_bloque = f // 5  # 5 bloques de 1M valores por bloque a escribir
    tam_max = 100 * 1024 * 1024  # 100MB

    print('Cantidad de valores a escribir:', N)

    # truncar archivo si existe
    with open(nombre, 'w'):
        pass

    # escribir datos
    N_restantes = N
    tam_actual = 0
    while N_restantes > 0:
        cif = cifras_entero
        r = N_restantes % tam_bloque
        c = N_restantes // tam_bloque
        if c > 0:
            t = tam_bloque
        elif c == 0:
            t = r
        N_restantes -= t
        print('t =', t, ', N_restantes =', N_restantes)

        if tam_actual + t * (cif + 1) >= tam_max:
            t = (tam_max - tam_actual) // (cif + 1)
            if t == 0:
                break

        with open(nombre, 'a+') as archivo:
            for _ in range(t):
                cifras_flotante = 6  # Limitar a 6 dígitos después del punto decimal
                entero = str(randint(10 ** (cif - 1), 10 ** cif - 1))  # Asegurar que el número entero tenga cifras exactas
                flotantes = [str(round(uniform(0, 1), cifras_flotante)) for _ in range(cif)]
                linea = [entero] + flotantes
                random.shuffle(linea)
                archivo.write(' '.join(linea) + '\n')

        tam_actual = os.path.getsize(nombre)

    if tam_actual > tam_max:
        with open(nombre, 'rb+') as archivo:
            archivo.seek(tam_max - 1)
            archivo.truncate()

crear_archivo_de_datos('datos.txt')
