#Parametre olarak bir cümle alan ve bu cümleti Title Case hale çeviren fonksiyon yazınız.
phrase=input("Enter a phrase: ")
kelimeler = phrase.split()
n= len(kelimeler)
print(n)
print(kelimeler)
def turn(i) :
    kelime=[]
    for kelime in kelimeler:
        newph = kelime[0].upper() + kelime[1: ].lower()
       
        print(newph, end=" ")
    
print(turn(n))
    


