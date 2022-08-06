#Parametre olarak bir cümle(string) alan ve kelime dizisi return eden bir fonksiyon yazınız.
cümle1= input("Enter a line:")
cümle2=input("Enter another line: ")
newline=cümle2.split()
print(cümle2)
def goback(cümle,dizi) :
    return cümle, dizi
goback(cümle1,newline)

print(goback(cümle1,newline))

#Bir dizideki ikinci elemanı return eden fonksiyon yazınız.

n=list(input("Enter a sequence:"))
print(n)
def show(dizi):
    return n[1]
show(n)
print(show(n))

#Parametre olarak bir sayı ve bir sayı dizisi alan, eğer sayı listede varsa True, yoksa False dönen bir fonksiyon yazınız.
p= int(input("Enter a number:"))
def check(liste,sayi):
    for a in liste:
        if sayi == a :
            return(True)

    else:
        return(False)
print(check([1,5,6,2,8,7,5,3,65,65,4,35,351,531],p))
