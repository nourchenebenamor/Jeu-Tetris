#projet de:
#Benamor nourchene
#Feleh ghofrane 

from Tetramino import Tetramino
from Point import Point
from Interface import KST

class Tetris:
    def __init__(self, Plateau):
        self.plateau_tetris = Plateau
        self.inMotion = Tetramino()

    def freeze(self):
        self.plateau_tetris.ajoutTetraMatrice(self.inMotion)
        self.plateau_tetris.effaceLigne()  
        self.inMotion = Tetramino()

    def mouvement(self, touche):
        if touche == KST.DROITE and self.inMotion.canMoveRight(self.plateau_tetris.matrice):
            self.inMotion.mouvementDroit()
        elif touche == KST.GAUCHE and self.inMotion.canMoveLeft(self.plateau_tetris.matrice):
            self.inMotion.mouvementGauche()
        elif touche == KST.BAS and not self.inMotion.checkCollision(self.plateau_tetris.matrice, Point(0, 1)):
            self.inMotion.gravity(1)
        elif touche == KST.ESPACE:
            self.inMotion.GRAVITYFORCE(self.plateau_tetris.matrice)
        elif touche == KST.HAUT:
            self.inMotion.tourner()

    def gravity(self, tick):
        if tick % 100 == 0 and not self.inMotion.checkCollision(self.plateau_tetris.matrice, Point(0, 1)):
            self.inMotion.gravity(1)

    def checkGravityAndSpawn(self, ):
        if self.inMotion.checkCollision(self.plateau_tetris.matrice, Point(0, 1)):
            self.freeze()

    def dessiner(self, Interface):
        self.inMotion.dessiner(Interface)