#projet de:
#Benamor nourchene
#Feleh ghofrane 

from Point import Point
from Interface import KST
from random import randint
class Tetramino:
    def __init__(self, ):
        liste_formes = ["straight", "square", "T", "L", "skew"]
        indice_aleatoire = randint(0, len(liste_formes) - 1)
        self.forme = liste_formes[indice_aleatoire]
        self.vecteur_points = []
        self.isDown = False
        self.invis = False

        if self.forme == "straight":
            self.vecteur_points = [Point(6, 0), Point(7, 0), Point(8, 0), Point(5, 0)]
            self.couleur = (40, 40, 240)
        elif self.forme == "square":
            self.vecteur_points = [Point(6, 0), Point(7, 0), Point(6, 1), Point(7, 1)]
            self.couleur = (213, 180, 11)
        elif self.forme == "T":
            self.vecteur_points = [Point(4, 0), Point(3, 0), Point(5, 0), Point(4, 1)]
            self.couleur = (65, 7, 203)
        elif self.forme == "L":
            self.vecteur_points = [Point(4, 0), Point(5, 0), Point(6, 0), Point(4, 1)]
            self.couleur = (213, 180, 11)
        elif self.forme == "skew":
            self.vecteur_points = [Point(4, 1), Point(5, 0), Point(4, 0), Point(3, 1)]
            self.couleur = (213, 11, 11)

        self.vecteur_position = self.vecteur_points[0]

    def dessiner(self, Interface):
        if not self.invis:
            for point in self.vecteur_points:
                Interface.curseur(point.abscisse, point.ordonne)
                Interface.write(" ", Interface.COULEUR['blanc'], self.couleur)

    def gravity(self, vitesse):
        for point in self.vecteur_points:
            point.ordonne += vitesse

    def checkCollision(self, matrice, direction):
        for point in self.vecteur_points:
            new_point = point + direction
            if new_point.ordonne >= 20 or new_point.abscisse < 0 or new_point.abscisse >= 10:
                return True
            if matrice[new_point.abscisse, new_point.ordonne] != 0:
                return True
        return False

    def canMoveRight(self, matrice):
        return not self.checkCollision(matrice, Point(1, 0))

    def canMoveLeft(self, matrice):
        return not self.checkCollision(matrice, Point(-1, 0))

    def mouvementDroit(self):
        for point in self.vecteur_points:
            point.abscisse += 1

    def mouvementGauche(self):
        for point in self.vecteur_points:
            point.abscisse -= 1

    def GRAVITYFORCE(self, matrice):
        while not self.checkCollision(matrice, Point(0, 1)):
            self.gravity(1)


    def calculAvantTourner(self,compteur):
        x = self.vecteur_position.abscisse - (self.vecteur_points[compteur].ordonne - self.vecteur_position.ordonne)
        y = self.vecteur_position.ordonne + (self.vecteur_points[compteur].abscisse - self.vecteur_position.abscisse)
        
        if x > 9 :
            Tetramino.mouvementGauche(self)
            Tetramino.calculAvantTourner(self,compteur)
        
        if x < 0 :
            Tetramino.mouvementDroit(self)
            Tetramino.calculAvantTourner(self,compteur)
        
        return x,y

    def tourner(self):
        rotated = False
        if not self.forme == "square" :
            liste=[self.vecteur_position]
            for compteur in range(1,len(self.vecteur_points)):
                x,y = Tetramino.calculAvantTourner(self,compteur)
                
                if not ( x < 0 or x > 9 ) :
                    liste.append(Point(x,y)) 
                 
            if len(liste) == 4 :
                self.vecteur_points = liste 
                rotated = True
        return rotated

    def mouvement(self, touche, matrice):
        if touche == KST.HAUT:
            self.tourner()
        elif touche == KST.DROITE and self.canMoveRight(matrice):
            self.mouvementDroit()
        elif touche == KST.BAS and not self.checkCollision(matrice, Point(0, 1)):
            self.gravity(1)
        elif touche == KST.GAUCHE and self.canMoveLeft(matrice):
            self.mouvementGauche()
        elif touche == KST.ESPACE:
            self.GRAVITYFORCE(matrice)