# -*- coding: utf-8 -*-

class A():
    sinifdegiskeni="A sınıfı"
    def __init__(self):
        self.a="b"
        
    def getir(self):
        return self.a


class B(A):
    def __init__(self):
        super().__init__()
        self.b="b"
        

o1 =B()

print(o1.getir())

print(o1.sinifdegiskeni)


class A():
    deger=10

class B(A):
    deger=12
    
class A(B):
    pass

o1 = A()

print(o1.deger)