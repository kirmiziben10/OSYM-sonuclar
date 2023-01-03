#2021 yılında OSYM tercih sonuçlarının ne zaman açıklanacağını söylemediğinden dolayı yapılmıştır.
#Kullanmak için sadece çalıştırmanız yeterli, konsoldan size bilgi verecektir. "python guncelleme.py"
#Telegram botu vs. haline getirilebilir?

import requests
import time
import os
from playsound import playsound#pip install playsound

degisti = False #Sonuçların başlamadan önce açıklanmadığı kabul ediliyor. Çalıştırdıktan sonra siteyi bir kez manuel olarak kontrol etmelisiniz.
kontrolSayisi = 1
eski = False #Eski site yok. İlk döngüden sonra gelecek.
kontrolAraligi = 60 #saniye

#Konsolu temizle.
def Temizle():
    os.system('cls' if os.name=='nt' else 'clear')#Çalıntı??!!

#İnternet ile alakalı hata kodları alınıp deneniyor.
def HataAyikla(r):
    if r.status_code == 200:
        return
    else:
        print(r.status_code + ' Hata kodu ile karşılaşıldı.')
        print('Sistemin "Soğuması" için kontrol aralığı artırılıyor')
        kontrolAraligi += 5
        #degisti = True #Hata ile karşılaştığında durmamalı!
        return

def SonuclariAl():
    r = requests.get('http://sonuc.osym.gov.tr', verify=False) # Umarım yerel ağda kötü biri yoktur.
    return r

while not degisti:
    yeni = SonuclariAl()
    HataAyikla(yeni)
    if not eski: #Sadece ilk döngüde çalışır.
        eski = yeni
        Temizle()
        print('İlk kontrol başarılı! sonuc.osym.gov.tr sitesini kontrol et.\nİstediğin sonuç henüz yoksa değişiklik olduğunda bu ses ile sana haber vereceğiz.')
        playsound('bildirim.wav')
        time.sleep(10)
        continue
    elif yeni.text == eski.text:
        kontrolSayisi += 1
        Temizle()
        print('Kontrol ' + str(kontrolSayisi) + ' tamamlandı.') #Debug, istenirse silinebilir.
        time.sleep(kontrolAraligi)
        continue #Tekrar dene.
    else:
        degisti = True
        print("Sonuçlar Güncellendi!")#İstediğiniz sonuç mu yoksa başka bir sonucun mu açıklandığını kendiniz kontrol etmelisiniz.
        playsound('bildirim.wav')
        break
