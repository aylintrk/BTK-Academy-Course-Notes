# 1-1000 arasında sayı var.Bulana kadar deniyelim. Bilgisayar girilen sayıyı asıl sayıdan büyük mü küçük mü diye belirlesin.
#oyunun kaç hamlede tamamlandığını ekrana basınız.
import random
count=0
num= random.randint(0,10)
while True:
    guess= int(input("Enter a number: "))
    if guess== num:
        print("Tebrikler bildiniz!")
        count += 1
        break
    elif guess>num :
        print("Daha küçük")
        count += 1
    else:
        print("Daha büyük")
        count += 1
print("",count,"hamlede tahmin ettiniz.")
print("Oyunu bitir.")
