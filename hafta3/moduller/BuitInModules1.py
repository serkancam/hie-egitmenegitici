from datetime import datetime, timedelta, timezone
import os
import time

zaman =  datetime.now()
print(zaman)
print(zaman.year)
zamanbiz= datetime(2018,10,7,12,27,30)

print(zamanbiz)

zamanbiz+= timedelta(days=8)
print(zamanbiz)

print(os.getcwd())
# os.mkdir("ilk")
print(os.sep)
print(os.name)

# liste = [str(zaman.year),str(zaman.month),str(zaman.day),str(zaman.hour)]
# os.chdir(r"/home/serkancam/Belgeler/test")
# os.makedirs(r"/".join(liste

print(os.listdir("/home/serkancam/Belgeler/test"))

print(os.walk("/home/serkancam/Belgeler/test"))

a,b,c = os.walk("/home/serkancam/Belgeler/test")

