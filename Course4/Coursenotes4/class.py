

class personel():
    def __init__(self,isim) :
        print("personel metodu çalıştı")
        self.isim= isim  
    def selamla(self):
        print("Merhaba", self.isim)

per1=personel("Ahmet")
per2=personel("Ayşe")
print(per1.isim)
print(per2.isim)
per1.selamla()
per2.selamla()