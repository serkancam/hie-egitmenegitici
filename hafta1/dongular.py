#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 10:03:08 2020

@author: serkancam
"""
#%% for dongusu
harfler = "abcdef"

for h in harfler:
    print(h, sep="-")

dir(harfler)

liste =["a","b","c",1,2,3]

for a in liste:
    print(a)
    
    
sozluk  = {"kitap":"book","bilgisayar":"computer","dil":"language"}

for i in sozluk:
    print(i)

for i in sozluk.items():
    print(i)

for i in sozluk:
    print(i,"--->",sozluk[i])

for i in range(5,1,-1):
    print(i)


#%% while dongusu

i=0
while i<10:
    print(i)
    i+=1


while True:
    try:
        a = int(input("birinci sayıyu giriniz:"))
        break
    except:
        print("1.sayıyı hatalı girdiniz:")
while True:
    try:
        b = int(input("ikinci sayıyu giriniz:"))
        break
    except:
        print("2. sayıyı hatalı girdiniz:")

print(f"{a}+{b}={a+b}")
    
    






































