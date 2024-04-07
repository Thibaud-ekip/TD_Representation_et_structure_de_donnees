import matplotlib.pyplot as plt

class Hashtable:

    def __init__(self,hash_function,length):
        "create a table"
        self.__length = length
        self.__hash = hash_function
        self.__table = [[] for i in range (length)]

    def put(self,key,value):
        "add a (key,value) in the table"
        index = self.__hash(key)%self.__length
        for couple in self.__table[index]:
            if couple[0] == key:
                couple[1] = value
        self.__table[index] = [(key,value)]+self.__table[index]

    def get(self,key):
        index = self.__hash(key)%self.__length
        for couple in self.__table[index]:
            if couple[0] == key:
                return couple[1]
        return None

    def repartition(self,n):
        "graph of number of couple per value of hashf"
        X = []
        Y = []
        for i in range (self.__length):
            X.append(i)
            Y.append(len(self.__table[i]))
        width = 1/n
        plt.bar(X, Y, width, color="blue")
        plt.show()

    def resize(self):
        "resize the hashtable"
        h = Hashtable(self.__hash,2*self.__length)
        for box in self.__table:
            for couple in box:
                h.put(couple[0],couple[1])
        self.__table = h.__table
        self.__length = 2*self.__length

    def sizeup(self):
        if sum([len(box) for box in self.__table])>1.2*self.__length:
            self.resize()

    def length(self):
        return self.__length

def h(str):
        res=0
        i=0
        for letter in str:
            res+=ord(letter)*33**i
            i+=1
        return res


if __name__ == '__main__':

    H=Hashtable(h,2)      #test
    H.put('a',1)
    H.put('b',2)
    assert(H.get('a')==1)
    H.put('c',3)
    H.sizeup()
    assert(H.length()==4)
    H.repartition(1.5)


    words=[]
    f = open('frenchssaccent.dic','r')
    for ligne in f:
        words.append(ligne[0:len(ligne)-1])
    f.close()

    L = Hashtable(h,320)      #table with 320 entrys
    for word in words:
        L.put(word,len(word))
    L.repartition(1)

    K = Hashtable(h,10000)    #table with 10000 entrys
    for word in words:
        K.put(word,len(word))
    K.repartition(1)










