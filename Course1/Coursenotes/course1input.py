#Input Example:1

income= input("Enter your income: ")
income= int(income)
tax_percent=0.18
tax_value= income* tax_percent
print("Your tax value: ",tax_value)

#Input Example:2(with strings)

string3= input("Enter your string for the code: ")
print(string3[0:len(string3):2])
print(string3[:len(string3):2])
print(string3[0::2])
print(string3[::2])
print(string3[1::2])

#Input Example:3

a= int (input("Enter your number: "))
if a<3:
    print("a is less than 3")
    print("c")
    print("Result!")
elif a == 3:
    print("a is equal to 3")
else:
    print("a is greater than 3 ")

#Input Example:4

sum_of_ages=0
for i in  range(3):
    birth_date= input("Enter the birth dates:")
    sum_of_ages += 2022- int(birth_date)
print(sum_of_ages/3)

