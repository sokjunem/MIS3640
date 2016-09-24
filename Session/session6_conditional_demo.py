'''
age = int(input('How old are you? '))


if age >=21:
    print('Your age is ', age)
    print('Your age is {}.' .format(age)) # Same answer with different coding
    print('Your age is ' + str(age) + '.')# Same answer with different coding
    print('Yes, you can.')
elif age >=6:
    print('Your age is ', age)
    print('Your are a teenager. No, you cannot.')
else:
    print('Your age is ', age)
    print('No, not allowed.')


if age >= 6 and age < 18:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')


# Nested conditionals
x = 1
y = 2
if x == y :
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')

# Exercise 1_1
weight = float(input('Enter your weight in kg: '))
height = float(input('Enter your height in m: '))

BMI = weight / (height**2)

if BMI <= 18.5:
    print('Your BMI is %.1f and underweight' % BMI)
elif BMI <= 24.9:
    print('Your BMI is %.1f and normal weight' % BMI)
elif BMI <= 29.9:
    print('Your BMI is %.1f and overweight' % BMI)
else:
    print('your BMI is %.1f and Obesity' % BMI)
'''
# Exercise 1_2

a = 
b = 
if a and b = str()
    print('string involved')