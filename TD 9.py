class Polynome:

    def __init__(self,q,n,coeff):
        self.__q = q
        self.__n = n #modulo x^n+1
        self.__coeff = coeff
        self.modulo()


    def modulo(self):
        "transform a pol from R[x] into Z_q[x]/(x^n+1)Z_q[x]"
        coeff2 = []
        n=self.__n
        for i in range(len(self.__coeff)):
            if i<n:
                coeff2.append(self.__coeff[i])
            k = i//n
            if k >=1:
                coeff2[i%n] += (-1)**k * self.__coeff[i]
        for i in range(len(coeff2)):
            coeff2[i] = coeff2[i]%self.__q
        self.__coeff = coeff2

    def add(self, polynome):
        assert self.__n == polynome.__n
        assert self.__q == polynome.__q
        if len(self.__coeff) < len(polynome.__coeff):
            for i in range(len(self.__coeff)):
                polynome.__coeff[i] += self.__coeff[i]
            self.__coeff = polynome.__coeff
        else :
            for i in range(len(polynome.__coeff)):
                self.__coeff[i] += polynome.__coeff[i]
        self.modulo()


    def mult(self, polynome):
        assert self.__n == polynome.__n
        assert self.__q == polynome.__q
        coeff2 = [0 for i in range(len(polynome.__coeff) + len(self.__coeff))]
        for i in range(len(self.__coeff)):
            for j in range(len(polynome.__coeff)):
                        coeff2[i+j] += self.__coeff[i]*polynome.__coeff[j]
        self.__coeff = coeff2
        self.modulo()

    def scalar(self, c):
        "multiplies by a scalar"
        for i in range(len(self.__coeff)):
            self.__coeff[i] = self.__coeff[i]* c
        self.modulo()

    def rescale(self, r):
        "use the function modulo"
        self.__q = r
        self.modulo()

    def fscalar(self, r, a):
        coeff2 = []
        self.__q = r                          #new pol in Z_r[x]/(x^n+1)Z_r[x]
        for i in range (len(self.__coeff)):
            coeff2.append(int(self.__coeff[i]*a)%r)
        self.__coeff= coeff2
        self.modulo()

    def coeff(self):
        "return the coefficients of a pol"
        return self.__coeff

if __name__ == '__main__':

    A = Polynome(4,3,[1,4,6,2])
    B = Polynome(4,3,[1,1,3])
    A.add(B)
    assert A.coeff() == [0,1,1]

    C = Polynome(3,3,[1,2,4])
    C.mult(C)
    assert C.coeff() == [0,0,0]

    D = Polynome(6,2,[4,5])
    D.rescale(3)
    assert D.coeff() == [1,2]

    D.fscalar(3,1)
    assert D.coeff() == [1,2]








