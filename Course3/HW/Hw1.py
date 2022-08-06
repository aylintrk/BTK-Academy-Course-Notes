#Write a function that takes 2 numbers as a parameter and returns its average. To test the function, call it 3 times and test its accuracy.

for p in range(3) :
    num1,num2=int(input("Enter a number: ")),int(input("Enter a number: "))
    def ort(number1,number2):
        av=(number1+number2)/2
        return av
    print(ort(num1,num2))

# Using the method you wrote in the second question, print the average of the intervals between 1 and 100 on the screen.

lists=list(range(0,100))
print(lists, end="")
def ort(say):
    count=0
    for i in range(say):
        count += lists[i]
    return count/len(lists)
ort(100)
print(ort(100))

#Write a function that takes a list of numbers as a parameter and returns the average of the list. Try with 3 different lists to test the function.

Length= int(input("Enter the number of ch's in your list: "))
list=[]
for i in range(Length) :
    ch=int(input("Enter the charachters for the list:"))
    list.append(ch)
print(list)

def ort(say):
    count=0
    for i in range(say):
        count += list[i]
    return count/len(list)
ort(Length)
print(ort(Length))


#Write a function that takes a number as a parameter and prints its factorial. Then call the method with the number 5.

n= int(input("Enter a number:"))
def fact(sayi):
    facto=1
    for i in range(1,sayi+1):
        facto= facto*i
    return facto
fact(n)
print("",n,"!=",fact(n))
print(" 5 !=",fact(5))

# Using the function you wrote in question 4, print the factorial of all numbers between 1-20 on the screen.

for i in range(2,20) :
    def fact(sayi):
        facto=1
        for i in range(1,sayi+1):
            facto= facto*i
        return facto
    fact(i)
    print(fact(i))
"""
listo=[]
for i in range(n):
    ch=str(input("Enter a sequence: "))
    listo.append(ch)
print(listo)
"""
##################################################


#Write a function that takes an array as a parameter and return the maximum number.

listo=[]
def sequ(chrach):
    n=int(input("Enter the ch length: "))
    for i in range(n):
        ch=str(input("Enter a sequence: "))
        listo.append(ch)
    return max(listo)
sequ(listo)
print(listo)
print(sequ(listo))

##################################################

#Write a function that takes an array as a parameter and return the minimum number.

listo2=[]
def sequ(chrach):
    n=int(input("Enter the ch length: "))
    for i in range(n):
        ch=str(input("Enter a sequence: "))
        listo2.append(ch)     
    return min(listo2)
sequ(listo2)
print(listo2)
print(sequ(listo2))
################################################################################################


#Take a paragraph as input. Write all the words in the paragraph capitalized on the screen.

praragraf=input("metin:")
kelimeler=praragraf.split()
print(kelimeler)
for kelime in kelimeler: 
    yenikelime= kelime[0].upper()+ kelime[1:].lower()
    print(yenikelime,end=" ")

#Find average value between every intervals in 1-100.

lists=list(range(0,100))
def listort(lists):
    return sum(lists)/len(lists)

def q3():
    for i in range(2,100):
        liste=list(range(1,i+1))
        print(listort(liste))

q3()




