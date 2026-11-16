#projet de:
#Benamor nourchene
#Feleh ghofrane 

from pygame.locals import *
import numpy as np

class Plateau:
    def __init__(self, x, y):
        self.matrice = np.zeros((x, y),int)
        self.score = 0
        self.couleurs = [(0,0,0),(40,40,240),(213,180,11),(65,7,203),(213,180,11),(213,11,11)]
        self.continuer = True

    def f(self, x):
        if x == 1:
            return 40
        elif x == 2:
            return 200
        elif x == 3:
            return 300
        elif x == 4:
            return 1200
        else:
            return 0


    def effaceLigne(self):

        new_matrice = np.zeros_like(self.matrice)
        completed_lines = 0
        new_row = self.matrice.shape[1] - 1

        for row in range(self.matrice.shape[1] - 1, -1, -1):

            if not all(self.matrice[:, row]):
                new_matrice[:, new_row] = self.matrice[:, row]
                new_row -= 1
            else:
                completed_lines += 1

        self.matrice = new_matrice
        
        self.score += self.f(completed_lines)

        
    def ajoutTetraMatrice(self, T):

        for point in T.vecteur_points :
            if (point.ordonne == 0 ):
                self.continuer = False
                


        color = 0
        if T.forme == "straight" :
            color = 1
        elif T.forme =="square":
            color = 2
        elif T.forme =="T" :
            color = 3
        elif T.forme =="L" :
            color = 4
        elif T.forme == "skew" :
            color = 5
        for point in T.vecteur_points :
            self.matrice[point.abscisse,point.ordonne] = color 
         

    def dessiner(self, Interface):
        for x in range(self.matrice.shape[0]):
            for y in range(self.matrice.shape[1]):
                Interface.curseur(x, y)
                Interface.write("  ", Interface.COULEUR['blanc'], self.couleurs[self.matrice[x, y]])
                

    def gameOver(self,Interface) : 
        
        self.matrice = np.zeros((10, 10),int)
        self.dessiner(Interface)
        Interface.curseur(0,3)
        #Interface.taille_fonte_x = Interface.taille_fonte_x /10
        Interface.write("Game over", Interface.COULEUR['rouge'],Interface.COULEUR['noir'] )
        Interface.curseur(0,5)
        Interface.write("Score :"+ str(self.score), Interface.COULEUR['rouge'],Interface.COULEUR['noir'] )
        