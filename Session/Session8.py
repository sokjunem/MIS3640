# CubeRoot

x = int(input('Enter an integer: '))
ans = 0
while ans**3 < x:
    ans = ans + 1
if ans**3 != x:
    print(str(x) + ' is not a perfect cube')
else:
    print('Cube root of ' + str(x) + ' is ' + str(ans))

def cuberoot(x):
    x = int(input('Enter an integer: '))
    ans = 0
    if x > 0 :
        while ans**3 < x:
            ans = ans + 1
        if ans**3 != x:
            print(str(x) + ' is not a perfect cube')
        else:
            print('Cube root of ' + str(x) + ' is ' + str(ans))
    if x < 0 :


# CubRootGuessCheck
cube = 28
for guess in range(cube+1):
    if guess**3 == cube:
        print("Cube root of", cube, "is", guess)

# Better version
cube = -28
for guess in range(abs(cube)+1):
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
    print(cube, 'is not a perfect cube')
else:
    if cube < 0:
        guess = -guess
    print('Cube root of ' + str(cube) + ' is ' + str(guess))