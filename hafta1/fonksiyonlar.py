# -*- coding: utf-8 -*-

def ilkFonksiyon():
    pass

ilkFonksiyon()


def yazdir(deger):
    print(deger)
    
    
yazdir("merhaba")


def yazdir1(isim,mesaj="Nasılsın?"):
    print("Merhaba",isim,mesaj)

yazdir1("serkan")


def yazdir2(s1,s2):
    print(s1,s2)

yazdir2(s2="serkan",s1="çam")

def araba(marka,model,*ozellik):
    print("MArka",marka)
    print("Model",model)
    for i in ozellik:
        print(i)


topla = lambda s1,s2: s1+s2


print(topla(10,20))
    
