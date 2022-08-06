#4 adet sınıf oluşturun. Sınıflar aşağıdaki özelliklere sahip olmalıdır.

#Hayvan Sınıfı : Bütün hayvanların ortak özelliklerinin toplandığı sınıf olacak.
#Köpek Sınıfı : Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa köpeklere ait ek özellikler ve metodlar ekleyin.
#Kuş Sınıfı : Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa kuşlara ait ek özellikler ve metodlar ekleyin.
#Balık Sınıfı : Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa balıklara ait ek özellikler ve metodlar ekleyin.

class animals():
    class köpek():
        def __init__(self,ses,neredeyaşar) :
            self.ses=ses
            self.neredeyaşar=neredeyaşar
            print("Class oluşturuldu.")



    köpke=köpek("Köpekler hav diye ses çıkarılar.","Köpekler karada yaşarlar.")
    print(köpke.ses,köpke.neredeyaşar)

    class kuş():
        def __init__(self,ses,neredeyaşar) :
            self.ses=ses
            self.neredeyaşar=neredeyaşar
            print("Class oluşturuldu.")



    kuşçuk=kuş(" Kuşlar cik diye öterler.","Havada uçabilirler.")
    print(kuşçuk.ses,kuşçuk.neredeyaşar)

    class balık():
        def __init__(self,ses,neredeyaşar) :
            self.ses=ses
            self.neredeyaşar=neredeyaşar
            print("Class oluşturuldu.")



    paluk=balık("Balıklar gluk diye ses çıkarırlar.","Suda yaşarlar.")
    print(paluk.ses,paluk.neredeyaşar)
    
    class Personel():
        def __init__(self,sicil,ad,soyad,maas,birim):
            print("Personel sınıfı init çaılıştı")
            self.sicil = sicil
            self.ad = ad
            self.soyad = soyad
            self.maas = maas
            self.birim = birim
        
        def bilgiler(self):
            print("Sicil: {}, Ad: {}, Soyad: {}, Maas: {}, Birim:{}".format(self.sicil,self.ad, self.soyad,self.maas,self.birim))
    
        def zamYap(self,tutar):
            self.maas += tutar #self.maas = self.maas
    per1 = Personel("123","Yasin","GÜRBÜZ",5000,"İD")
    per1.bilgiler()
    per1.zamYap(100)
    per1.bilgiler()

    class Personel():
        def __init__(self,sicil,ad,soyad,maas,birim):
            print("Personel sınıfı init çaılıştı")
            self.sicil = sicil
            self.ad = ad
            self.soyad = soyad
            self.maas = maas
            self.birim = birim
        
        def bilgiler(self):
            print("Sicil: {}, Ad: {}, Soyad: {}, Maas: {}, Birim:{}".format(self.sicil,self.ad, self.soyad,self.maas,self.birim))
    
        def zamYap(self,tutar):
            self.maas += tutar #self.maas = self.maas
        
        def birimDegis(self,yBr):
            self.birim= yBr 
        
    class Yazilimci(Personel): #Burda Yazilimci sınıfını Personel sınıfından miras aldığımızı belirttik.
        pass #Bir bloğu sonradan tanımlamak istediğimiz zaman kullanılan bir deyimdir.
#Burada personel sınıfından miras aldığımız özellik ve methodları kullandık.
    yazilimci1 = Yazilimci("123","İsmail","AYDIN",5000,"BL")
    yazilimci1.bilgiler()