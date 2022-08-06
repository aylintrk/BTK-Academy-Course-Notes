#Get 2 inputs from the user. Compare these two numbers and write "Small number x and big number y" on the screen. 
x,y =int(input("Enter a number:")),int(input("Enter a number:"))
if x>y :
    print("x=",x, "is the biggest and " "y=",y,"is the smallest value")
    print ("küçük sayı {} ve büyük sayı {}".format(y,x) )
    print("küçük syayı" ,str(y) ," ve büyük sayı" ,str(x) )
else :
    print("y=",y,"is the biggest and" "x=",x, "is samllest value" )

# Write multiples of 7 from 0 to 100 with range.
# Write multiples of 7 from 0 to 100 with the for loop.
# Write multiples of 7 from 0 to 100 with a while loop.
# Put the multiples of 7 from 0 to 100 in a list. Write the square of all the elements in this list on the screen.

import numbers
import datetime
start = datetime.datetime.now()
#####

print(list(range(0,100,7)))

#####

for i in range(0,100,7) :
    print(i)
#####

number=0
while number%7==0 and number<=100:
    print(number)
    number += 7

#####
liste=list(range(0,101,7))
print(list(range(0,101,7)))
nw=[]
for i in range(0,101,7) :
    nw.append(i*i)
print(nw)
print(i*i for i in liste)

for i in liste:
    print(i*i)

endtime=datetime.datetime.now()
print(endtime-start)

# Roll a rigged dice. This dice has a 6% chance of getting 6.

#1

import random 
Marble=[1,2,3,4,5,6]
random.randrange(0,101)
if random.randrange(0,101)==6:
    print("6")
else:
    print(random.randrange(1,6))
    
#2

number=random.randint(1,3)
if number== 1:
    print(6)
else:
    print(random.randint(1,6))