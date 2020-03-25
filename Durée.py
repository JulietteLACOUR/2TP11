class Duree:

    def __init__(self, heure, minute, seconde):
        self.__H = heure
        self.__M = minute
        self.__S = seconde

    def getH(self):
        return self.__H

    def getM(self):
        return self.__M

    def getS(self):
        return self.__S

    def __str__(self):
        return str(self.__H)+"h"+str(self.__M)+"m"+str(self.__S)+"s"

    def __add__(self, D):
        NewS = self.__S + D.getS()
        retenue = 0
        while NewS >= 60:
            retenue += 1
            NewS -= 60
        NewM = self.__M + D.getM() + retenue
        retenue = 0
        while NewM >= 60:
            retenue += 1
            NewM -= 60
        NewH = self.__H + D.getH() + retenue
        return Duree(NewH, NewM, NewS)

if __name__== '__main__':
   d1 = Duree(5, 7, 8)
   d2 = Duree(9, 0, 56)
   d3 = d1 + d2
   print(d1)
   print(d2)
   print(d3)

