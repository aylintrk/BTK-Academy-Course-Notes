from re import A

#Find the letter "a" from the input string/line with for loop.

Line=input("Enter the Line or Word: ")
count=0
for i in range(len(Line)):
    if Line[i]=="a" :
        count += 1
print(count)        

#Get 5 inputs from the user, and find the average of them.

total=0
for i in range(5) :
    nums=input("Enter 5 numbers to see the result: ")
    nums= int(nums)   
    total += nums 

print(total/5)

#Get a input and make the given strings first letter in its capitilize form,rest will be in its lower case form.(use the upper/lower) 

import string


stringx=input("Enter your line for the adjusment: ")
After= stringx[0].upper() + stringx[1:].lower()
print(After)
