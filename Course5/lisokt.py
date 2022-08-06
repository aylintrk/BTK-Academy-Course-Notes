
#yanyana virgüllü de yazılabilir.
""""
print(liste)
print(len(liste))
print(len(liste[0]))
print(liste[0])
print(liste[0][0])
print(liste[-1])
print(liste[-1][-1])"""

#lstenin tüm elemanlarını print et teker teker.

#listeyi tersten yaz 
#2 boyutlu birlistenin tüüm elemnalrını bir arrtııran

def printlist(liste):
    for i in liste:
        for j in i :
            print(j)

def increaselist(liste):
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            liste[i][j] +=1 
    return liste
def reverselist(liste):
    print([i[::-1] for i in liste[::-1]])
liste=[
    [1,2,3,6,9],
    [4,5,6,1],
    [7,8,9]
]

printlist(liste)


def printlist(liste):
    for i in liste:
        for j in i :
            print(i)
liste = [
    [1,2,3,6,9],
    [4,5,6,1],
    [7,8,9]
]

printlist(liste)
liste=increaselist(liste)
print(liste)
reverselist(liste)


