from math import sqrt

def diskriminant(a,b,c):
     return b**2-4*a*c

def roots(a,b,c):
     D=diskriminant(a,b,c)

     if D<0:
          return ("Рівняння немає жодного кореня")
     elif D==0:
          x=-b/(2*a)
          return ("рівняння має корінь: x={x}") 
     else:
      x1=(-b - sqrt(D))/(2*a)
      x2=(-b + sqrt(D))/(2*a)
     return ("Рівняння має корені: x1={x1}, x2={x2}")

a=-12
b=3
c=23

print (roots (a,b,c))

