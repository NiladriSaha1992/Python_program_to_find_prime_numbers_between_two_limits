"""
Example of List Comprehension
----------------------------------------------------------------------------------------

Write a python script to create a list of prime numbers between two limits, where the values of the two limits must be taken from the user.

"""

sl = int(input("Enter a position from where to start searching: "))
el = int(input("Enter a postion at where to end searching: "))
def getPrimeNumber(n):
  isPrime = True
  for e in range(2, n):
    if(n % e == 0):
      isPrime = False
      break
  if isPrime == True:
    return n

primeNumbers = [getPrimeNumber(e) for e in range(sl, el+1)]

while primeNumbers.count(None) > 0:
  primeNumbers.remove(None)

print(primeNumbers)