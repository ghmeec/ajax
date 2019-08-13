
import math
last_item=20

# Codes for ajax groups
# last_item is the nth item in the series
# trig,hyperbolic,exponential functions are implemented based on Taylor series
#the functions largely utilizies Taylor series 


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

# logarithm functions



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

def sine(angle):
    angleInRadians=degress_to_radians(angle);
    sineOf=0
    for n in range(0,last_item):
        a=power(-1,n)
        b=power(angleInRadians,(2*n)+1)
        c=math.factorial((2*n)+1)
        sineOf=sineOf+((a*b)/c)

    return sineOf

def cosine(angle):
    angleInRadians=degress_to_radians(angle);
    cosineOf=0
    for n in range(0,last_item):
        a=power(-1,n)
        b=power(angleInRadians,(2*n))
        c=math.factorial((2*n))
        cosineOf=cosineOf+((a*b)/c)

    return cosineOf

def tangent(angle):
    tangentOf=sine(angle)/cosine(angle)
    return tangentOf




# exponent
def exponent(number):
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

def arcsine(angle):
    arcsineOf=0
    for n in range(0,last_item):
        a=math.factorial(2*n)
        b=power(angle,((2*n)+1))
        c=(power(4,n))*((2*n)+1)*(power(math.factorial(n),2))
        arcsineOf=arcsineOf+((a*b)/c)

    return radians_to_degrees(arcsineOf)

def arccosine(angle):
    arccosineOf=radians_to_degrees((math.pi/2.0))-arcsine(angle) 
    return arccosineOf

def arctan(angle):
    arctanOf=0.0
    for n in range(0,last_item):
        a=power(-1,n)
        b=(2*n)+1+0.0
        c=power(angle,((2*n)+1))

        arctanOf=arctanOf+((a*c)/b)
    return radians_to_degrees(arctanOf)
    

def arcsinh(angle):
    arcsinhOf=0
    for n in range(0,last_item):
        d=power(-1,n)
        a=math.factorial(2*n)
        b=power(angle,((2*n)+1))
        c=(power(4,n))*((2*n)+1)*(power(math.factorial(n),2))
        arcsinhOf=arcsinhOf+((a*b*d)/c)
    return arcsinhOf

print arctan(1)

