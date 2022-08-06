import random
from subprocess import _TXT
def createpass(length):
    password=""
    for i in range(length):
     password=random.choice("abcdefghjklmnoprstuwxvyz")   
        return password

passwords=[createpass(random.randrange(5,15)) for i in range(10000)
with open("passwords.txt","W",encoding="")