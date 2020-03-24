class Complex:

    def __init__(self, réelle, imaginaire):
        self.__R = réelle
        self.__I = imaginaire

    def getR(self):
        return self.__R

    def getI(self):
        return self.__I

    def __add__(self, C):
        if isinstance(C, Complex) == True:
            return Complex(self.__R + C.getR(), self.__I + C.getI())

    def __sub__(self, C):
        if isinstance(C, Complex) == True:
            return Complex(self.__R - C.getR(), self.__I - C.getI())

    def __mul__(self, C):
        if isinstance(C, Complex) == True:
            return Complex(self.__R * C.getR() - C.getI()*self.__I, self.__I * C.getR() + self.__R*C.getI())

    def __truediv__(self, C):
        if isinstance(C, Complex) == True:
            Numerateur = self * Complex(C.getR(),C.getI())
            return Complex(Numerateur.getR() * (C.getR()**2-C.getI()**2), Numerateur.getI() * (C.getR()**2-C.getI()**2))

    def __abs__(self):
        return (self.__R**2+self.__I**2)**(1/2)

    def __eq__(self, C):
        if isinstance(C, Complex) == True:
            return self.__R == C.getR() and self.__I == C.getI()

    def __ne__(self, C):
        if isinstance(C, Complex) == True:
            return self.__R != C.getR() and self.__I != C.getI()

    def __str__(self):
        return "parte réelle : R="+str(self.__R)+" et partie imaginaire : I ="+str(self.__I)

if __name__== '__main__':
   c1 = Complex(2,5)
   c2 = Complex(3,7)
   c3 = c1 + c2
   c4 = c1 - c2
   c5 = c1 * c2
   c6 = c1 / c2
   c7 = abs(c1)
   c8 = c1 == c2
   c9 = c1 != c2
   print(c1)
   print(c2)
   print(c3)
   print(c4)
   print(c5)
   print(c6)
   print(c7)
   print(c8)
   print(c9)
