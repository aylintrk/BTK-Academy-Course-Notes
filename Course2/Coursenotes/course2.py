list5=[1,2,3,4,5,6,7,8,9,10]
print(list5[4])
print(list5[1::2])
print(list5[::2])

print(len(list5))
print(sum(list5))
print(max(list5))
print(min(list5))

#Print the average of the numbers in the list5.

print(sum(list5)/len(list5))
total=0
for i in range(len(list5)) :
    total += list5[i]
print(total/10)

#Find the sum of the fist half of the list5 and sum of the last haf of the list. Find the difference between them.

firsthalf= list5[:len(list5) // 2]
lasthalf= list5[len(list5) // 2:] 
print(sum(firsthalf)- sum(lasthalf))


#Find the max and min difference from the list5.

print(max(list5)-min(list5))
#The mix of two list
list1=[1,2,3,4,5,6,7,8,9,10]
list2=[97,98,99]
newlist=list1+ list2 
print(newlist)

#How to make list with interval

print(list(range(0,20)))
print(list(range(10,20)))
print(list(range(10,20,2)))

# Print all even numbers between 0-100 with the Range method.
print(list(range(0,100,2)))
# Print all odd numbers between 100,200 with the Range method.
print(list(range(101,200,2)))
# Write it with the Range method, from 1000 to 0, decreasing in multiples of 100.
print(list(range(1000,0,-100)))
print(list(range(1000,-1,-100)))
#Changing the list elements
for number in range(100) :
    print(number/2)

# Print the square of all even numbers between 0-50 on the screen.
for i in range(0,50,2) :
    print(i**2)

#Easy acces to changing the forms of the lists

list4=[1,2,3,4,5]
print(list4)

list4.append(10)
print(list4)

print(list4.insert(0,20))   #Insert does not properlywork in print, you have to enter print as a new line under it to add.
print(list4)

list4.insert(0,20)
print(list4)

list4.sort()
print(list4)

list4.sort(reverse=True)
print(list4)

list4.pop()
print(list4)

print(list4.pop())
print(list4)

print(list4.pop(1))
print(list4)

# Write append(99) using insert.

list6=[1,2,3,4,5]
print(list6)
list6.insert(len(list6),99)
print(list6)

#Examples of making new lists from a given list.

list7=[1,2,3,4,5]
newlist2= []
for i in range(len(list7)) :
    newlist2.append(list7[i]**2)
print(newlist2)

newlist=[]
for i in list7:
    newlist.append(i**2)
print(newlist)

newlist2= [ i**2 for i in list7]
print(newlist2)

#Some examples for list form changing
list7=[1,2,3,4,5]
newlist2= [ i**2 for i in list7]
print(newlist2)


newlist3=[i + 1 for i in newlist2]
print(newlist3)

newlist3= [i / 2 for i in newlist2]
print(newlist3)


#Increase all elements of the new list by 1 with list comprehension.

for i in list7:
    newlist3=[i + 1 for i in newlist2]
print(newlist3)

#Divide the elements of the list.

for i in list7:
    newlist3= [i / 2 for i in newlist2]
print(newlist3)

#Printing different type of Lists.

for i in range(0,10,2):
    print(i)

for i in range(10) :
    if i % 2 == 0:
        print(i)

#Examples of print command.
num5=5
print(num5)
print()
num5= int(num5)
num5 += 1
print(num5)

print(num5+100)
print(num5)

num5=num5 +1
print(num5)

num5=str(num5)
num5= num5+str(1)
print(num5)

num5= num5+ "5" 
print(num5)

#While loop

#Example:1

number2=10
while number2<20:
    print(number2)
    number2 += 1

#Example:2

number2=0
while number2<100:
    print(number2)
    number2 += 2
    if number2>50 :
        break

#Example:3

num3=0
while num3 != -1 :
    num3=int(input("Enter a number: "))
    print(num3)

#Example:4

num4=10
while num4<20:
    print(num4)
    num4 += 1

#Example:5

x=0
while x <10:
    x += 1
    if x == 5 :
        continue
    print(x)

# Using random command

#Example:1

import random
print(random.randrange(1,10))
print(random.randrange(1,10))

liste=[x for x in "abcdefghjkllmnoprstuvwxyz"]

print(random.choice(liste))

#Example:2

import random 
marb=[1,2,3,4,5,6,6,6,6,6]
experimentcount=100
resultexp=[]
for i in range(experimentcount):
    exp=random.choice(marb)
    resultexp.append(exp)
print(resultexp)
print(resultexp.count(1)/ experimentcount)
print(resultexp.count(2)/ experimentcount)
print(resultexp.count(3)/ experimentcount)
print(resultexp.count(4)/ experimentcount)
print(resultexp.count(5)/ experimentcount)
print(resultexp.count(6)/ experimentcount)