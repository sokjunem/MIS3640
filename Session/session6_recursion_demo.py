'''
def countdown(n):
    if n <= 0:
        print('Blastofffactorial')
    else:
        print(n)
        countdown(n-1)

countdown(3)

def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print('n = ', n)
    print_n(s, n-1)

print_n('Hello', 3)

# for recursion: needs ending point and something to get there
'''
def factorial(x):
    if x == 1:
        return 1  
    print('curent x = ', x)
    return x * factorial(x-1)

print(factorial(7))

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(3))
print(fib(10))