class Tree:
    def __init__(self,label,*children):
        "create a node"
        self.__label = label
        self.__children = children

    def label(self):
        return self.__label

    def children(self):
        return self.__children

    def nb_children(self):
        return len(self.__children)

    def child(self,i):
        return self.__children[i]

    def is_leaf(self):
        return self.__children==()

    def depth(self):
        if self.is_leaf():
            return 0
        return 1 + max([child.depth() for child in self.__children])

    def __str__(self):
        "represent a tree as a string"
        if self.is_leaf():
            return f'{self.__label}'
        else:
            res=''
            for child in self.__children:
                res = res + ',' + child.__str__()
            return f'{self.__label}' + f'{res}'

    def eq(self,__value:object):
        return self.__str__()==__value.__str__()


    '''
    def deriv(self,var:str):                 #  i don't understand how to create this method
        varbis=Tree(var)
        for child in self.__children:
            if

    '''

import unittest


class TestTree(unittest.TestCase):

    def test_label(self):
        t= Tree('f', 'g', 'k')
        self.assertEqual(t.label(), 'f')
    def test_children(self):
        t= Tree('f', 'g', 'k')
        self.assertEqual(t.children(), ('g','k'))
    def test_nb_children(self):
        t= Tree('f', 'g', 'k')
        self.assertEqual(t.nb_children(), 2)
    def test_is_leaf(self):
        t= Tree('f', Tree('g'), Tree('k'))
        t2= Tree('f')
        self.assertEqual(t.is_leaf(), False)
        self.assertEqual(t2.is_leaf(), True)
    def test_child(self):
        t= Tree('f', 'g', 'k')
        self.assertEqual(t.child(1), 'k')
        self.assertEqual(t.child(0), 'g')


if __name__ == '__main__':
    t1 = Tree('f', Tree('2',Tree('4')), Tree('3'))
    t2 = Tree('f', Tree('2',Tree('4')), Tree('3'))
    t3 = Tree('f', Tree('2',Tree('6')), Tree('3'))
    print(t1 == t2)
    print(t1 == t3)
    unittest.main()

