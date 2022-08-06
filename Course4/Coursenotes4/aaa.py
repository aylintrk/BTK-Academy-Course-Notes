

decimal=ord('a')
print(decimal)
decimal=ord('b')
print(decimal)
decimal=ord('c')
print(decimal)

print(chr(97))

print(chr(ord('a')+1))
print()

text= "hello world"
for i in text:
    print(chr(ord(i)+1))

#Parametre olarak bir text ve sayı alın ,metni sayı kadar sağa kaydıran ve return eden sezar şifreleme algoritması fonksyonu yazınız.
def sezar(text2,number):
    newtext=""
    for i in text2:
        newtext +=(chr(ord(i)+number))
    return newtext
print(sezar("merhaba",3))
print(sezar("phukded",-3))

################################################""""
"""listo=[45,78,94,12,56,89,1,2,5,7]
aranansayı=3
buldumu=False
counter=0
for i in listo:
    if i==aranansayı :
        print("Sayı bulundu!")
        buldumu=True
        break
if not buldumu:
    print("Sayı bulunumadı")
print(counter,"defa bulundu")
    """

#####################################################
#Bir listedebir elemanın kaç kere geçtiğini bulunuz.
listo=[45,78,94,12,56,89,1,2,5,7,1,1,1,5,5,5,5,5,5,5,5,45]

def ara(sayı):
    count =0
    buldumu=False
    for i in listo:
        if i==sayı :
            print("Sayı bulundu!")
            buldumu=True
            print(listo.count(sayı))
            break
    if not buldumu:
        print("Sayı bulunumadı")
ara(5)

print()

#Parametre olarak bir liste ve bir sayı alan bir fonksiyon yazınız.bu fonksiyon,liste içerisinde sayıların kaçkere geçtiğini bulup return ediniz.
def search(listop,sayi):
    buldumu=False
    counter=0
    for i in listo:
        if i==sayi :
            buldumu=True
            return(listo.count(sayi))

listop=[45,78,94,12,56,89,1,2,5,7,1,1,1,5,5,5,5,5,5,5,5,45]
print("5," ,search(listop,5), "defa bulundu.")
