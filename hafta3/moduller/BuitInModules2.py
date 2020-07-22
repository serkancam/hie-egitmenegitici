# -*- coding: utf-8 -*-

import sys 
for item in sys.argv:
    if item == "Merhaba":
        isim = input("isminizi giriniz:")
        print("Hoş geldiniz", isim,"memnun oldum.")
        


print(*sys.path,sep="\n")
    