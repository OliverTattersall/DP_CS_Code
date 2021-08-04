import math

#input requirements: sides a,b and one of either theta or side c. Theta must be inbetween sides a and b. 
# put None for missing value. Theta should be in degrees
def calCosLaw(a, b, c, theta):
    try:
        if c==None:
            a=int(a)
            b=int(b)
            theta=int(theta)
            c=(a**2+b**2-2*a*b*math.cos(theta*(math.pi/180)))**(1/2)
            return c
        if theta==None:
            a=int(a)
            b=int(b)
            c=int(c)
            theta = math.acos((c**2-a**2-b**2)/(-2*a*b))
            return theta*(180/math.pi)

    except:
        return "failure to meet requirements"

    return "failure to meet requirements"
print(calCosLaw(4, 6, None, 10))