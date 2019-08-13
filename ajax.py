
import math

def add(*args):
    total=0
    for i in args:
        total=total+i
    return total

def subsract(*args):
    if(len(args)==0):
        return "No argument supplied"
    difference=args[0]
    for i in  range(1,len(args)):
        difference=difference-args[i]
    return difference

def multiply(*args):
    if(len(args)==0):
        return "No argument supplied"

    product=args[0]
    for i in  range(1,len(args)):
        product=product*args[i]

    return product



def division(divider, quotient=1.0):
    if quotient == 0:
        return "the quotient shouldnt be zero"
    return divider/quotient

def square(base=0):
    exponent=2
    return base**exponent

def cube(base=0):
    exponent=3
    return base**exponent

def power(base=0,exponent=0):
    return base**exponent

def logarithm(number,base):
    exponent=0
    for i in range(50):
        if(power(base,i)==number):
            exponent=i
    
    return exponent

def degress_to_radians(degrees):
    return math.pi * degrees/180.0

def radians_to_degrees(radians):
    return radians*180.0/math.pi

def inverse(number):
    return power(number,-1)

#factorial
def recur_factorial(n):  
   if n == 1:  
       return n  
   else:  
       return n*recur_factorial(n-1)

def permutations(n,r):
    return recur_factorial(n)/recur_factorial(n-r)

# trig functions

def sine(angle,last_item):
    angleInRadians=degress_to_radians(angle);
    sineOf=0
    for n in range(0,last_item):
        a=power(-1,n)
        b=power(angleInRadians,(2*n)+1)
        c=math.factorial((2*n)+1)
        sineOf=sineOf+((a*b)/c)

    return sineOf

def cosine(angle,last_item):
    angleInRadians=degress_to_radians(angle);
    cosineOf=0
    for n in range(0,last_item):
        a=power(-1,n)
        b=power(angleInRadians,(2*n))
        c=math.factorial((2*n))
        cosineOf=cosineOf+((a*b)/c)

    return cosineOf

def tangent(angle,last_item):
    tangentOf=sine(angle,last_item)/cosine(angle,last_item)
    return tangentOf



# exponent
def exponent(number):
    last_item=20
    exp=0
    for n in range(0,last_item):
        a=power(number,n)+0.0
        b=math.factorial(n)+0.0
        exp=exp+(a/b)
      
    return exp    




#hyberbolic functions
def cosh(number):
    coshOf=0
    a=exponent(number)+0.0
    b=exponent(0-number)+0.0
    coshOf=coshOf+((a+b)/2)
    return coshOf

def sinh(number):
    sinhOf=0
    a=exponent(number)+0.0
    b=exponent(0-number)+0.0
    sinhOf=sinhOf+((a-b)/2)
    return sinhOf

def tanh(number):
    a=sinh(number)
    b=cosh(number)
    tanhOf=a/b
    return tanhOf

# nth power 
def nth_root(number, n):
    nth_root_of=0.0
    nth_root_of=nth_root_of+power(number,inverse(n))
    return nth_root_of

print nth_root(7,2)
