#Exercise 3
import math

def mysqrt(a):
    x = 5
    while True:
        y = (x + (a/x)) / 2
        if y == x:
            break
        x = y
    print(y)
mysqrt(1)


def test_square_root(a):
    for i in range(1, 10):
        diff = (mysqrt(a) - math.sqrt(a))
        print(a, mysqrt(a), math.sqrt(a), diff)

print(test_square_root(1))


input()