#class######################
from convert import convertweekdays

class personel():
    def __init__(self,isim,soyad,yaş,cinsiyet,maaş,calişma_gunleri) :
        self.isim= isim 
        self.soyad=soyad
        self.yaş=yaş
        self.cinsiyet=cinsiyet
        self.maaş=maaş 
        self.calişma_gunleri =calişma_gunleri
    def printinfo(self):
        print(self.isim,self.soyad, self.yaş, "yaşındadır" )
        print("MAaşı",self.maaş,"Cinsiyeti",self.cinsiyet)
        #print( "Çalışma günleri", [convertweekdays(i) for fori in self.calişma_gunleri])
        #print( "Çalışma günleri",self.calişma_gunleri)
        #for i in self.calişma_gunleri:
        #    print(convertweekdays[i])
        gunler= [convertweekdays[i] for i in self.calişma_gunleri]
        print( "Çalışma günleri","/" .join(gunler))
        return
    def maas_guncelle(self,yeni_maaş):
        self.maaş=yeni_maaş
#Çalışma günü ekleme func yazınız.
#Gün olarak sayı alsın ve listenin içine append ile eklensin.
    def calişma_gunu_ekle(self,gun):
        self.calişma_gunleri.append(gun)
per1=personel("Ahmet","kara","67","erkek","15k",[1,3,5])
per2=personel("Ayşe","baş","25","kadın","15k",[1,4,7])
per3= personel("Enes","tan","41","erkek","20k",[2,6,7])

personellistesi= [per1,per2,per3]
print(convertweekdays[personellistesi[0].calişma_gunleri[2]])
print()
per1.printinfo()
per2.printinfo()
per3.printinfo()

per1.maas_guncelle(20000)
per1.calişma_gunu_ekle(6)
per1.printinfo()