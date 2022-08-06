#dictionary

dict= {
    "beyaz" : "white" ,
    "orange" : "turuncu",
    "siyah": "black"
}
print(dict["beyaz"])
print(dict.keys())
print(dict.values())
print(dict.items())

for key,value in dict.items():
    print(key,value)

dict["mavi"]=" blue"
print(dict)

#set

list=[1,2,3,4,5,5,6,5,6,6,7,7,7,7,7,8,9,9]
print(list)

nwlist= set(list)
print(nwlist)

#tuple

a=(1,1,2)
print(a)

print(len(["hello"]))
print(len("hello"))

print("hello"[0])
print(["hello"][0])

#######functions#####

def f(x):
    print(2*x)
    
def g(a):
    print(3*a)

print("hello world")
f(2)
print("hello world")
f(3)
print("hello world")
g(10)

######################


def f(x):
    print(2*x)
    return 1

print(f(2))

def f(x):
    return(2*x)

print(f(2))

def f(x):
    return(3*x)
   
answr= f(2)
print(answr)

def f(x,y):
    res= x+ x*y-1
    return res
   
print(f(2,3))
print(f(5,10))

# Parametreolarak 2 taneintalın ve küçük olanı return eden min adında fonk yazınız.
def min(x,y):
    if x<y:
        return x 
    else :
        return y 
print(min(5,10))
print(min(10,5))
print(min(3,8))
print(min(1,1000))

# Kullanıcıdan 2 adet input alınız.Kçük olanın minumum fonskiyonu ile ekrana basınız.
num1,num2 = int(input("Enter the numbers")),int(input("Enter the numbers"))

def minimum(num1,num2):
    if num1<num2:
        return num1
    return num2

print(minimum(num1,num2))
print("küçük sayı: ",minimum(num1,num2))
########

def fonksiyonu(b,a):
    print(b)
    print(a)

a=5
b=3
fonksiyonu(a,b)

#How to organize the functions:

#receive list as input from user
def yontem1():
    list=[]
    while True:
        sayı=input("say gir :")
        if sayı=="":
            break
        list.append(int(sayı))

    print(list)

def yontem2():

#receive list as input from user
    liste=[]
    uzunluk=int(input("list uzunluk"))
    for i in range(uzunluk):
        sayy=int(input("say gir:"))
        liste.append(sayy)
    print(liste)

def yontem3():

#receive list as input from user
    strl_list=input("List gir:")
    liste=strl_list.split("")
    liste=[int(i)for i in liste]
    print(liste)

def orthesap():
    say1=int(input("1:"))
    say2=int(input("2:"))
    print(orthesap(say1),orthesap(say2))


yontem1()


