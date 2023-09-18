# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 16:12:36 2023

@author: Candelaria
"""

import matplotlib.pyplot as plt #aqui esta la funcion que nos permite graficar
import time #permite establecer un tiempo inicial y uno final 
import random #Genera numeros aleatorios en un rango
from nodo import Nodo

class ListaDobleEnlazada:
    """Representa una lista doblemente enlazada.

    Esta clase implementa una lista doblemente enlazada con métodos
    para agregar, insertar, extraer, copiar, invertir, ordenar y
    concatenar elementos, además provee funcionalidad de
    visualización y seguimiento del tamaño de la lista.

    Attributes:
        cabeza (Nodo): El primer nodo de la lista.
        cola (Nodo): El último nodo de la lista.
        tamanio (int): El número de elementos en la lista.

    """
    
    def __init__(self):
        self.cabeza = None  
        self.cola = None   
        self.tamanio = 0        
        
    def esta_vacia(self):
        """Verifica si la lista está vacía.

        Returns:
            bool: True si la lista está vacía, False en caso contrario.

        """
        return self.tamanio == 0
      
    def tamanio(self):
        return self.tamanio
    
    def agregar_al_inicio(self, dato):
        """Agrega un elemento al inicio de la lista.

        Args:
            dato: El elemento que se va a agregar.

        """

        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamanio += 1
    
    def agregar_al_final(self, dato):
        """Agrega un elemento al final de la lista.

        Args:
            dato: El elemento que se va a agregar.

        """

        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamanio += 1

    def insertar(self, dato, posicion=None):
        """Inserta un elemento en la posición especificada.

        Args:
            dato: El elemento que se va a insertar.
            posicion (int, opcional): La posición en la que se va a insertar el elemento.
                Si no se especifica, se agrega al final de la lista.

        Raises:
            IndexError: Si la posición está fuera de rango.

        """
        if posicion is None:
            self.agregar_al_final(dato)
        elif posicion == 0: 
            self.agregar_al_inicio(dato)
        else:
            nuevo_nodo = Nodo(dato)
            actual = self.cabeza
            for _ in range(posicion - 1):
                if actual is None:
                    raise IndexError("Posición fuera de rango")
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            if actual.siguiente is not None:
                actual.siguiente.anterior = nuevo_nodo
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual
            self.tamanio += 1
    
    def extraer_primero(self):
        """Extrae el primer elemento de la lista.

        Returns:
            El primer elemento de la lista.

        Raises:
            IndexError: Si la lista está vacía.

        """
        if self.esta_vacia():
            raise IndexError("La lista está vacía")
        dato = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        if self.cabeza is not None:
            self.cabeza.anterior = None
        else:
            self.cola = None
        self.tamanio -= 1
        return dato

    def extraer_ultimo(self):
        """Extrae el último elemento de la lista.

        Returns:
            El último elemento de la lista.

        Raises:
            IndexError: Si la lista está vacía.

        """
        if self.esta_vacia():
            raise IndexError("La lista está vacía")
        dato = self.cola.dato
        self.cola = self.cola.anterior
        if self.cola is not None:
            self.cola.siguiente = None
        else:
            self.cabeza = None
        self.tamanio -= 1
        return dato        
    
    def extraer(self, posicion=None):
        """Extrae un elemento de la posición especificada.

        Args:
            posicion (int, opcional): La posición del elemento que se va a extraer.
                Si no se especifica, se extrae el último elemento.

        Returns:
            El elemento extraído.

        Raises:
            IndexError: Si la posición está fuera de rango o si la lista está vacía.

        """
        if posicion == -1:
            posicion = self.tamanio-1

        if self.esta_vacia():
            raise IndexError("La lista está vacía")
        if posicion is None:
            posicion = self.tamanio - 1
        if posicion < 0 or posicion >= self.tamanio:
            raise IndexError("Posición fuera de rango")

        if posicion == 0:
            return self.extraer_primero()
        elif posicion == self.tamanio - 1:
            return self.extraer_ultimo()
        else:
            actual = self.cabeza
            for i in range(posicion):
                actual = actual.siguiente
            anterior = actual.anterior
            siguiente = actual.siguiente
            anterior.siguiente = siguiente
            siguiente.anterior = anterior
            self.tamanio -= 1
            return actual.dato
        
    def copiar(self):
        """Crea una copia de la lista.

        Returns:
            ListaDobleEnlazada: Una nueva lista que es una copia de la lista actual.

        """
        nueva_lista = ListaDobleEnlazada()
        actual = self.cabeza
        while actual is not None:
            nueva_lista.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return nueva_lista
    
    def invertir(self):
        """Invierte el orden de los elementos en la lista."""
        actual = self.cabeza
        while actual is not None:
            actual.anterior, actual.siguiente = actual.siguiente, actual.anterior
            actual = actual.anterior
        self.cabeza, self.cola = self.cola, self.cabeza
        
    def ordenar(self): #metodo insercion
        """Ordena los elementos de la lista en orden ascendente."""
        if self.tamanio <= 1:
            return
    
        actual = self.cabeza.siguiente
    
        while actual is not None:
            valor_actual = actual.dato
            nodo_anterior = actual.anterior
    
            while nodo_anterior is not None and nodo_anterior.dato > valor_actual:
                nodo_anterior.siguiente.dato = nodo_anterior.dato
                nodo_anterior = nodo_anterior.anterior
    
            if nodo_anterior is None:
                self.cabeza.dato = valor_actual
            else:
                nodo_anterior.siguiente.dato = valor_actual
    
            actual = actual.siguiente
            
    def concatenar(self, otra_lista):
        """Concatena esta lista con otra lista.

        Args:
            otra_lista (ListaDobleEnlazada): La lista que se concatenará.

        Raises:
            TypeError: Si el argumento no es una instancia de ListaDobleEnlazada.

        """
        if isinstance(otra_lista, ListaDobleEnlazada):
           # nueva_lista = self.copiar()
            actual = otra_lista.cabeza
            while actual is not None:
                self.agregar_al_final(actual.dato)
                #nueva_lista.agregar_al_final(actual.dato)
                actual = actual.siguiente
            #return nueva_lista
        else:
            raise TypeError("Se espera una LDE como argumento")
    
    def __iter__(self):
        """Itera sobre los elementos de la lista."""
        actual = self.cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente
   
    def __add__(self, otra_lista):
        """Concatena esta lista con otra lista.

        Args:
            otra_lista (ListaDobleEnlazada): La lista que se concatenará.

        Returns:
            ListaDobleEnlazada: Una nueva lista que es la concatenación de ambas listas.

        Raises:
            TypeError: Si el argumento no es una instancia de ListaDobleEnlazada.

        """
        if isinstance(otra_lista, ListaDobleEnlazada):
            nueva_lista = self.copiar()  # Copiar la instancia actual
            actual = otra_lista.cabeza
            while actual is not None:
                nueva_lista.agregar_al_final(actual.dato)
                actual = actual.siguiente
            return nueva_lista
        else:
            raise TypeError("Se espera una LDE como argumento")

    def __str__(self):
        """Obtiene una representación en cadena de la lista."""
        elementos = []
        actual = self.cabeza
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " <-> ".join(elementos)
    
    def __len__(self):
        """Obtiene el tamaño de la lista."""
        return self.tamanio
    
    
