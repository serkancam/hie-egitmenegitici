# -*- coding: utf-8 -*-

#%% polimorfizm

class Ulke1():
    def yer():
        print("Ülke 1 Asyada ")
    def tip():
        print("Ulke1 federal cumhuriyet")
    def nufus():
        print("80 Milyo2")


class Ulke2():
    def yer():
        print("Ülke 2 Avrupada ")
    def tip():
        print("Ulke2 kraliyet")
    def nufus():
        print("200 Milyon")

def fonk(nesne):
    nesne.tip()
    nesne.yer()
    nesne.nufus()

