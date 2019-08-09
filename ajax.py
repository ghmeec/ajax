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

print inverse(5)