
# Write a function that takes a number as a parameter and returns the factorial of the number.

n=int(input("enter a number :"))
 
def fact(number):
    answer= 1
    for i in range(1,n+1):
        answer= answer*i
    return answer
print(fact(n))
import math 
print(math.factorial(4))
print(math.pow(2,4))

def factorial(num: int) -> int :
    answer= 1
    return answer 

    #Write a function that takes a number as a parameter and returns true if odd and false if odd.

num= int(input("enter a number: "))

def iseven(num):
    if num%2==0 :
        return True
    return False

def iseven(num):
    return num%2==0

print(iseven(num))


#Write a function that takes a number as a parameter and finds whether that number is prime or not.

def isprime(num):
    for i in range(2,num//2):
        if num%i==0:
            return False
    return True
print(isprime(num))


#Using isprime method, print all prime numbers between 90 and 1000.
for i in range(90,1000):
    if isprime(i):
        print(i)
    else:
        print("Bu sayı asal değilidir")

##########
def selamla(isim):
    print("Merhaba " + isim )


for i in range(5):
    name = input("Enter your name: ")
selamla(name)


#Write a function that takes a number as a parameter and prints a star pyramid of that size.

n= int(input("n= "))
def star(sayi) :
    for i in range(1,n+1):
        print("* "*i)
star(n)
