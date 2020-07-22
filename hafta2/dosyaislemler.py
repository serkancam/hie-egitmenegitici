# -*- coding: utf-8 -*-

# Dosya işlemelri
# metin tabanlı dosyalar (csv,xml,json,bson,txt,html)

#dosya = open("dosya_yolu","r",encoding="utf-8")

def dosyaAc(adres):
    import os
    if os.path.exists(adres):
        return open(adres,"r+")
    else:
        return open(adres,"w+")
    
dosya = dosyaAc("defter.csv")

#yazmak write,writelines

dosya.write("Ali;Veli;123\n")

liste = ["Deneme;Deneme;981\n","Deneme;Deneme;981\n"]
dosya.writelines(liste)

dosya.flush()#dosya kapatmadan dosya işlemlerini yansıtır. kapatmadan kayıt yapar

#okuma read,readline,readlines
dosya.seek(0)
print(dosya.read(5))


dosya.seek(0)
print(dosya.readline(2))


dosya.seek(0)
print(dosya.readlines())

#diğerleri
#tell,seek,truncate,flush,close

print(dosya.tell())#imlecin yerini getirir


dosya.seek(10)
dosya.truncate()
dosya.seek(0)
print(dosya.read())


dosya.close()

