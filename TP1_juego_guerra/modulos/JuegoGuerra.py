from carta import Carta 
from mazo import Mazo
import random  

valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
palos = ['♠', '♥', '♦', '♣']
class JuegoGuerra:
    
    """Simula el juego de cartas guerra.

    En este juego, dos jugadores compiten para ganar todas las cartas
    disponibles. El juego consiste en turnos donde los jugadores
    revelan cartas y, en función de sus valores, pueden ganar cartas
    de su oponente o enfrentar una "Guerra".

    Attributes:
        mazo (Mazo): El mazo de cartas inicial para el juego.
        jugador1 (Mazo): El mazo del jugador 1.
        jugador2 (Mazo): El mazo del jugador 2.
        turnos (int): El número de turnos jugados en el juego.

    """

    def __init__(self):
        
        self.mazo = Mazo()
        self.mazo.mazo = [Carta(valor, palo) for valor in valores for palo in palos]
        random.shuffle(self.mazo.mazo)
        
        self.jugador1 = Mazo()
        self.jugador2 = Mazo()
        for _ in range(26): #se reparten las cartas entre los dos jugadores.
            self.jugador1.poner_arriba(self.mazo.sacar_arriba())
            self.jugador2.poner_arriba(self.mazo.sacar_arriba())
        
        self.turnos = 0
    
    def jugar_turno(self):
        """Realiza un turno del juego.
        
        """
        self.turnos += 1
        carta_jugador1 = self.jugador1.sacar_arriba()
        carta_jugador2 = self.jugador2.sacar_arriba()
        
        if carta_jugador1 is None or carta_jugador2 is None:
            return

        print(f'Turno: {self.turnos}')
        print(f'Jugador 1:')
        
        for _ in range(len(self.jugador1.mazo)):
            print(f'-X', end=" ")
        print("\n")
        print(f'Jugador 2:')
        
        for _ in range(len(self.jugador2.mazo)):
            print(f'-X', end=" ")

        print(f'\n           {carta_jugador1} {carta_jugador2}')
        

        if valores.index(carta_jugador1.valor) > valores.index(carta_jugador2.valor):
            self.jugador1.poner_abajo(carta_jugador1)
            self.jugador1.poner_abajo(carta_jugador2)
        
        elif valores.index(carta_jugador1.valor) < valores.index(carta_jugador2.valor):
            self.jugador2.poner_abajo(carta_jugador1)
            self.jugador2.poner_abajo(carta_jugador2)
        
        else:
            self.jugar_guerra()

    def jugar_guerra(self):
        """Maneja la Guerra durante el juego.

        """
        print("\n                 **** Guerra!! ****")
        guerra_cartas = [self.jugador1.sacar_arriba(), self.jugador2.sacar_arriba()]
        
        for _ in range(3):
            carta_jugador1 = self.jugador1.sacar_arriba()
            carta_jugador2 = self.jugador2.sacar_arriba()
            
            if carta_jugador1 is not None and carta_jugador2 is not None:
                guerra_cartas.extend([carta_jugador1, carta_jugador2])

        print(f'Turno: {self.turnos}')
        print(f'Jugador 1:')
        
        for _ in range(len(self.jugador1.mazo)):
            print(f'-X', end=" ")
        print("\n")
        print(f'Jugador 2:')
        
        for _ in range(len(self.jugador2.mazo)):
            print(f'-X', end=" ")

        print(f'\n           {guerra_cartas[0]} {guerra_cartas[1]}')

        if valores.index(guerra_cartas[0].valor) > valores.index(guerra_cartas[1].valor):
            self.jugador1.mazo.extend(guerra_cartas)
        
        else:
            self.jugador2.mazo.extend(guerra_cartas)

    def jugar(self):
        
        """Inicia el juego y continúa los turnos hasta un límite (10000 turnos) o un ganador.

        Continúa ejecutando turnos del juego hasta que se alcance
        un límite de turnos (empate) o uno de los jugadores gane.

        Returns:
            str: El resultado del juego (ganador o empate).

        """
        
        while self.turnos < 10000:
            
            self.jugar_turno()
            if self.jugador1.esta_vacio():
                print("\n---------------------------------")
                print("      ***** Jugador 2 gana la partida *****")
                return "Jugador 2"
            
            elif self.jugador2.esta_vacio():
                print("\n---------------------------------")
                print("      ***** Jugador 1 gana la partida *****")
                return "Jugador 1"
        
        print("\n---------------------------------")
        print("      ***** EMPATE *****")
        return "Empate"

#if __name__ == "__main__":
#    juego = JuegoGuerra()
#   ganador = juego.jugar()
#   print(f"Resultado final: {ganador}")                   




