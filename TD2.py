import math

class Fraction:

    def __init__(self,num,den):
        self.__den=den
        self.__num=num

    def simplify(self):
        pgcd=math.gcd(self.__num,self.__den)
        self.__num= self.__num//pgcd
        self.__den=self.__den//pgcd
        self.value=self.__num/self.__den
        self.look= f"{self.__num} / {self.__den}"

    def add(self,fraction):
        self.__num=self.__num*fraction.__den+fraction.__num*self.__den
        self.__den=self.__den*fraction.__den
        self.value=self.__num/self.__den
        self.look= f"{self.__num} / {self.__den}"

    def mult(self,fraction):
        self.__den=self.__den*fraction.__den
        self.__num=self.__num*fraction.__num
        self.value=self.__num/self.__den
        self.look= f"{self.__num} / {self.__den}"

if __name__ == '__main__':     #test
    c = Fraction(2,5)
    d = Fraction(4,5)
    c.mult(d)
    d.add(Fraction(2,5))
    d.simplify()
    assert(c.value==0.32)
    assert(d.value==1.2)
    print(c.look)
    print(d.look)


H=Fraction(0,1)
for i in range (1,1000):    #doing it until 10000 exceeds the limit of integer
    H.add(Fraction(1,i))
print(H.value)


L=Fraction(0,1)
for i in range (1000):      #doing it until 10000 exceeds the limit of integer
    L.add(Fraction((-1)**i,2*i+1))
print(L.value)



'''
class Polynomial:
    def __init__(self,coef):
        self.__coef=coef
        self.__str=''

    def __str__(self):
        self.__str=''
        i=0
        for coef in self.__coef:
            if coef==1:
                self.__str= 'X**i+'+self.__str
                i+=1
            elif coef!=0:
                self.__str= '{coef}*X**i+'+self.__str
                i+=1
        if res[-1] == '+':
            self.__str = self.__str[:-1]
'''



