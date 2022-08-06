#parametre olarak bir liste alın ve bu listeyi sıralayıp return eden bir fonksiyon yazınız.
def sort(liste):
    yeniliste=[]
    while len(liste)>0:
        enbuyuk=max(liste)
        yeniliste.append(enbuyuk)
        liste.remove(enbuyuk)
        print(yeniliste)
    return yeniliste

liste=[1,2,3,4,5,6,7,8,3,2,6,8,4,4,4,32213]
print(sort(liste))