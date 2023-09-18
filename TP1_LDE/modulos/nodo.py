class Nodo:
    """Representa un nodo en una lista doblemente enlazada.

    Un nodo contiene un dato y referencias al siguiente nodo y al nodo anterior.

    Attributes:
        dato: El dato almacenado en el nodo.
        siguiente (Nodo): Referencia al siguiente nodo en la estructura (por defecto None).
        anterior (Nodo): Referencia al nodo anterior en la estructura (por defecto None).
    
    """
    def __init__(self, dato):
        
        self.dato = dato
        self.siguiente = None
        self.anterior = None