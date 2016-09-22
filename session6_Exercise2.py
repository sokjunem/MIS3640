import math
# Exercise 2_3

def gcd(a, b):
    if b == 0:
        return a
    else:
        r = a - (int(a/b) * b)
        return gcd(b, r)
      
print(gcd(1780,250))

# Exercise 2_4

def move(n, source, bridge, destination):
    if n == 1:
        print('%s ---> %s' % (source, destination))
   

   
input()
