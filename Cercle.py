class Cercle:
    def __init__(self, rayon):
        self.__R = rayon

    def getR(self):
        return self.__R

    def __add__(self, C):
        if isinstance(C, Cercle) == True:
            return Cercle(self.__R + C.getR())

    def __lt__(self, C):
        if isinstance(C, Cercle) == True:
            return self.__R < C.getR()

    def __gt__(self, C):
        if isinstance(C, Cercle) == True:
            return self.__R > C.getR()

    def __str__(self):
        return "Rayon du cercle : R="+str(self.__R)


if __name__== '__main__':
   c1 = Cercle(2)
   c2 = Cercle(3)
   c3 = c1 + c2
   c4 = c1 < c2
   c5 = c2 > c3
   print(c1)
   print(c2)
   print(c3)
   print(c4)
   print(c5)
