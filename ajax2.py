import math
from itertools import product

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

def fibonnaci():
    #   Change this value for a different result
    nterms = 40

    #   uncomment to take input from the user
    #   nterms = int(input("How many terms? "))

    #   check if the number of terms is valid
    if nterms <= 0:
        print("Plese enter a positive integer")
    else:
        print("Fibonacci sequence:")
        for i in range(nterms):
            number=recur_fibo(i)
            if(number%2==0):
                if number>4000000:
                    break
                print(number)


fibonnaci()
#largest prime factor
# A function to find largest prime factor
#  
def maxPrimeFactors (): 
    n=600851475143
    # Initialize the maximum prime factor 
    # variable with the lowest one 
    maxPrime = -1
      
    # Print the number of 2s that divide n 
    while n % 2 == 0: 
        maxPrime = 2
        n >>= 1     # equivalent to n /= 2 
          
    # n must be odd at this point,  
    # thus skip the even numbers and  
    # iterate only for odd integers 
    for i in range(3, int(math.sqrt(n)) + 1, 2): 
        while n % i == 0: 
            maxPrime = i 
            n = n / i 
      
    # This condition is to handle the  
    # case when n is a prime number  
    # greater than 2 
    if n > 2: 
        maxPrime = n 
      
    return int(maxPrime) 

print "Max prime factor is : "+str(maxPrimeFactors ())

def is_palindrome(num):
    return str(num) == str(num)[::-1]

multiples = ( (a, b) for a, b in product(xrange(100,999), repeat=2) if is_palindrome(a*b) )

products=max(multiples, key=lambda (a,b): a*b)
print "The Largset Palindrome factor : "+ str( products)
print "The Largset Palindrome  : "+ str(products[0]*products[1])

