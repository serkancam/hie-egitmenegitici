# -*- coding: utf-8 -*-
s1="www.google.com"
s2 = "www.bing.com"
say=0


for i in s1,s2:
    for harf in i:
        if harf=="o":
            say+=1


print(f"o harfinden {say} adet vardır.")


from math import sqrt, log10, cos

print(sqrt(23))
print(log10(56))
print(cos(45))

#%% random

import random

liste  =  (random.randint(1000)) for i in range(20)

print(liste)