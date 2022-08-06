
# There are numbers between 1-1000. Let's try until we find it. Let the computer determine whether the entered number is greater or less than the original number.
#press the screen in how many moves the game is completed.
import random
count=0
num= random.randint(0,10)
while True:
    guess= int(input("Enter a number: "))
    if guess== num:
        print("Congrats!You've found it!")
        count += 1
        break
    elif guess>num :
        print("Go for smaller")
        count += 1
    else:
        print("Go for higher")
        count += 1
print("You've guessed it in your","",count,". move!")
print("You've finished the game!!.")
