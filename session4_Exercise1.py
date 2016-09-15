import math

def quadratic(a,b,c):
    discriminant = (b**2) - (4*a*c)
    if discriminant < 0 :
        print('The solution is two different imaginary root')
    elif discriminant == 0 :
        solution = -b / (2*a)
        print('There is one solution:', solution)
    else :
        solution1 = (-b + math.sqrt(discriminant)) / (2*a)
        solution2 = (-b - math.sqrt(discriminant)) / (2*a)
        print('The solution is', solution1, 'or', solution2)

a = float(input('enter the number for a:'))
b = float(input('enter the number for b:'))
c = float(input('enter the number for c:'))

print(quadratic(a,b,c))

input()