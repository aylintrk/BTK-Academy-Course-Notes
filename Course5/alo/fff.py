def FirstFactorial(num):
  fact=1
  for i in range(1,num+1):
    fact = fact*i
  # code goes here
  return fact

# keep this function call here 
print(FirstFactorial(int(input())))