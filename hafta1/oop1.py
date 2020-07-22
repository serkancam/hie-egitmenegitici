# -*- coding: utf-8 -*-

f = lambda x:x*x

print(f(4))

#%%

harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
çevrim = {i: harfler.index(i) for i in harfler}
isimler = ["ahmet", "ışık", "ismail", "çiğdem",
"can", "şule", "iskender"]
print(sorted(isimler, key=lambda x: çevrim.get(x[0])))
print(isimler.sort())

#%%

class Kedi(): 
    tur = "felis" #class attribute
    def __init__(self,ad,yas,cinsiyet):#constructor
        self.adi=ad
        self.yasi=yas
        self.cinsiyeti = cinsiyet
    
    def Miyavla(self):
        print(self.adi,"Miyavladı")
    
    @classmethod
    def NefesAlma(cls):#sınıf methodu
        print("Bir",cls.tur,"Nefes aldı")


k1 = Kedi("pırtık",22,"erkek")
print(k1.adi)

#%% yapıcı yıkıcılar

class A:
    def __init__(self):#constructor
        self.a=1
        print("constructor çalıştı.")
    
    def __del__(self):#destructor
        print("Destructor çalıştı")
    

n1 =A()
del n1

#%% instance/sınıf parametresi

class A:
    sayi=0
    def __init__(self,param):
        self.param=param
        
    def f1(self):
        print(self.param)
        
    def f2(self):
        self.f1()
        
    @classmethod
    def f3(cls):
        print(cls.sayi)
        
#%% private 

# __gizli   gizilidir
# __gizli_  gizlidir
#__gizli__  gizli değil
#
#
class A:
    sayi=0
    __deger1=20
    def __init__(self,param,param2):
        self.param=param
        self.__param2=param2
        
    def f1(self):
        print(self.param)
        
    def f2(self):
        self.f1()
        
    @classmethod
    def f3(cls):
        print(cls.sayi)


#%% property ler
class A:
    sayi=0
    __deger1=20
    def __init__(self,param,param2):
        self.param=param
        self.__param2=param2
    
    
    @property
    def param2(self):
        return self.__param2
    
    @param2.setter
    def param2(self,gelen):
        if gelen:
            if isinstance(gelen,int):
                if 0<gelen<10:
                    self.__param2=gelen
    @param2.deleter
    def param2(self):
        self.__param2=2
    def f1(self):
        print(self.param)
        
    def f2(self):
        self.f1()
        
    @classmethod
    def f3(cls):
        print(cls.sayi)

a= A(3,5)
a.param2=7
print(a.param2)
del a.param2
print(a.param2)

        


        
