#projet de:
#Benamor nourchene
#Feleh ghofrane 

from Interface import Interface
from Point import Point
from Plateau import Plateau
from Tetris import Tetris

if __name__ == '__main__': 

    DIM_X, DIM_Y = 10, 20

    interface = Interface(DIM_X, DIM_Y, "Tetris")

    plateau = Plateau(DIM_X, DIM_Y)

    tetris = Tetris(plateau)

    canPress = True
    canPressCD = 15
    tick = 0
    
    while True:
        key = interface.lire_touche()
        if key is not None and plateau.continuer and canPress:
            tetris.mouvement(key)
            canPress = False

        if plateau.continuer :
            plateau.dessiner(interface) 
            tetris.dessiner(interface)
            tetris.gravity(tick)
        else: 
            canPress = False
            plateau.gameOver(interface)
        
        if canPressCD == 15:
            canPress = True
        else:
            canPressCD +=1

        interface.mise_a_jour()
        tetris.checkGravityAndSpawn()
        interface.pause(15)
        tick += 10