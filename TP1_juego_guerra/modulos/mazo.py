from carta import Carta
class Mazo:
    '''
    Representa un mazo de cartas.

    Un mazo es una colección de cartas que se puede manipular
    mediante operaciones como agregar cartas en la parte superior o
    inferior, sacar cartas de la parte superior y verificar si el
    mazo está vacío.

    Attributes:
        mazo (list): Una lista que almacena las cartas en el mazo.
        cabeza (Carta): La carta en la parte superior del mazo.
        cola (Carta): La carta en la parte inferior del mazo.
    '''
    def __init__(self):
        
        self.mazo = []  
        self.cabeza = None 
        self.cola = None  

    def poner_arriba(self, carta):        
        """Agrega una carta en la parte superior del mazo.

        Args:
            carta (Carta): La carta que se va a agregar.

        """
        self.mazo.insert(0, carta)
        self.cabeza = self.mazo[0]  
        if self.cola is None:  
            self.cola = carta

    def poner_abajo(self, carta):        
        """Agrega una carta en la parte inferior del mazo.

        Args:
            carta (Carta): La carta que se va a agregar.

        """
        self.mazo.append(carta)
        self.cola = self.mazo[-1] 
        if self.cabeza is None: 
            self.cabeza = carta

    def sacar_arriba(self): 
        """Saca y devuelve la carta en la parte superior del mazo.

        Returns:
            Carta: La carta en la parte superior del mazo, o None si el
                   mazo está vacío.

        """
        if not self.esta_vacio():
            carta = self.mazo.pop(0)
            if carta == self.cabeza:
                self.cabeza = self.mazo[0] if self.mazo else None  
            return carta

    def esta_vacio(self):        
        """Verifica si el mazo está vacío.

        Returns:
            bool: True si el mazo está vacío, False en caso contrario.

        """
        return len(self.mazo) == 0

    def __str__(self):
        """Devuelve una representación en cadena del mazo.

        Returns:
            str: Una cadena que representa todas las cartas en el mazo.

        """
        return ' '.join(str(carta) for carta in self.mazo)