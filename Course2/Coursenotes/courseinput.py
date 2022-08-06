#Get a input (age) and find out which school she/he should go to.

Age=int(input("Enter your Age: "))
if Age<0 or Age>120:
    print("Age is invalid")
elif Age>=0 and Age<=7:
    print("You dont go to any school.")
elif Age>=8 and Age<=13 :
    print("You are going to primary school.")
elif Age>=14 and Age<=19 :
    print("You are going to high school.")
elif Age>=19 and Age<=25 :
    print("You are going to university.")
else:
    print("You are going to your job.")


#Get inputs until user gets -1. Exit while loop at -1. Print the min/max and median of the previously entered numbers.

number=0
list=[]
while number != -1:
    number=int(input("Enter a number: "))
    if number != -1:
        list.append(number)
print(list)
print(max(list))
print(min(list))
print(sum(list))
print(sum(list)/len(list))

#Make random password out of your name.

import random
name=input("Enter your name: ")
name= name.lower() + name.upper() + "0123456789"
print(name)
password=""
for i in range(10) :
    password += random.choice(name)
print(password)

