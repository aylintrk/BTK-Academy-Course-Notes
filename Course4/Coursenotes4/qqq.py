#recursive functions
def examplerecursion(n):
    if n==0:
        return
    print(n)
    examplerecursion(n-1)
examplerecursion(5)
print()
"""
def examplerecursion(n):
    if n==0:
        return
    print(n)
    examplerecursion(n-1)
examplerecursion(5)"""

def a ():
    b()
    print(1)
    b()

def b():
    print(2)

a()
b()
print()
def examplerecursion(n):
    if n==0:
        return
    print(n)
    examplerecursion(n-1)
    print(n)
examplerecursion(5)
#pyhtontutor ile cheeck et bunu.
####################
def fact(n):
    if n==1:
        return 1 
    return n* fact(n-1)
print(fact(5))
#####################
