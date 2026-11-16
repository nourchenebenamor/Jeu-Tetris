#projet de:
#Benamor nourchene
#Feleh ghofrane 

class Point:
    def __init__(self, x, y):
        self.abscisse = x
        self.ordonne = y

    def __add__(self, vecteur):
        return Point(self.abscisse + vecteur.abscisse, self.ordonne + vecteur.ordonne)

    def __repr__(self):
        return f"Point : ("+str(self.abscisse)+","+str(self.ordonne)+")"