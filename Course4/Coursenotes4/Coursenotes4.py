def max1(liste):
    return max(liste)
print()
def max2(liste):
    enbuyuk=liste[0]
    for i in liste:
        if i> enbuyuk:
            enbuyuk=i
        print(enbuyuk)
    return enbuyuk

print(max1([232,23,54,56,89,57,34,5692,4832048,]))
print()
print(max2([232,23,54,56,89,57,34,5692,4832048,]))

def min(liste):
    enkucuk=liste[0]
    for i in liste:
        if i<enkucuk :
            enkucuk= i
        print(enkucuk)
    return enkucuk

print(min([232,23,54,56,89,57,3,5692,4832048,]))
############################################


