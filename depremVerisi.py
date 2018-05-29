import requests
from bs4 import BeautifulSoup
import datetime

r= requests.get("http://www.koeri.boun.edu.tr/scripts/lst1.asp")
soup =BeautifulSoup(r.content,"html.parser")

tumDepremListesi=(soup.find_all("pre"))
ay='%02d'% datetime.date.today().month
gun='%02d'% datetime.date.today().day
yil='%02d'% datetime.date.today().year

from datetime import datetime, timedelta
oncekiAySonGunTarihi= datetime.today()-timedelta(days=datetime.today().day)

j=int(gun)

while (j>-1):
    for liste in tumDepremListesi:
        if(j==0 and int(ay)==datetime.today().month):
            j=oncekiAySonGunTarihi.day
            ay='%02d'% oncekiAySonGunTarihi.month
            yil=oncekiAySonGunTarihi.year   
        tariheGoreBolunmusListe=(liste.text).split(str(yil)+"."+str( ay)+"."+str('%02d'% j))
        if(len(tariheGoreBolunmusListe)>1):

            print(str(yil)+"."+str(ay)+"."+str('%02d'% j)+" tarihinde "+str(len(tariheGoreBolunmusListe))+" tane deprem oldu")
        
    j-=1

