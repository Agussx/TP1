class Carta:
    """Representa una carta del juego.

    Una carta se caracteriza por su valor y su palo.

    Attributes:
        valor (str): El valor de la carta.
        palo (str): El palo de la carta.
        dato (str): Una cadena que combina el valor y el palo para representar la carta.

    """
    def __init__(self, valor, palo):
        
        self.valor = valor
        self.palo = palo
        self.dato = f'{valor}{palo}'

    def __str__(self):
        """Devuelve una representación en cadena de la carta.

        Returns:
            str: Una cadena que representa la carta.

        """
        return f'{self.valor}{self.palo}'