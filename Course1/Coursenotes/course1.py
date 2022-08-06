from operator import truediv
from ssl import VerifyFlags

# Basic Variables and Some Equaitons with Numbers

num=6
print(num,type(num))

orn_bool= True
print(orn_bool, type(orn_bool))

metin= "Hello World"
print(metin,type(metin))

num2= 3.5
print(num2,type(num2))

print(5/2)
print(5//2)
print(2**3)
print(100**0.5)

# The Importance of the Paranthese Placement

print(5+2/4)
print((5+2)/4)

# True/False Statements

#Example :1

print(5==5)
print(5 != 5)
print(5>4)

say= 5
say= say+1
print(say)
say +=2
print(say)
say *=2 
print(say)

print(True and False)
print(True or False or False)
print(not True)

#Example:2

liste=[1,2,3,4]
print(1 in liste)
print(1 not in liste)

# How to Print "Hello World" in Text Type Corretly

print('hello "world"')

try1= """
Hello        
world
"""
print(try1)
try2="Hello\nworld"
print(try2)

text1=" Hello" 
text2 ="world"
text3= text1+ " " +text2
print(text3)

# Strings

string2="Hello world"
print(type(string2))
print(len(string2))
print(string2.upper())
print(string2[0])
print(string2[10])
print(string2[1])
print(string2[-1])
print(string2[0:3])
print(string2[6:len(string2)])
print(string2[5:len(string2)])
print(string2[7:len(string2)])

print(string2[6:10:2])
print(string2[6:11:2])
print(string2[::-1])
print(string2[::-2])

# If-Else Stataments

a=5
if a<3:
    print("a is less than 3")
    print("c")
    print("Result!")
elif a == 3:
    print("a is equal to 3")
else:
    print("a is greater than 3 ")

for i in range(20) :
    print(i)

# Easy Access to Change the Form of The Lines

astring4="heLlO WoRlD"
print(astring4*3)
print(astring4.upper())
print(astring4.lower())
print(astring4.capitalize())
print(astring4.title())
print(astring4.swapcase())
print(astring4.count("a"))
print(astring4.find("a"))

#Printing the Strings Characters

for i in range(5):
    print(i,astring4[i])

#Changing The Letters in String
astring4="Hello World"
astring4= 'n'+ astring4[1:]
astring4= astring4[:-1] +'e'
print(astring4)






