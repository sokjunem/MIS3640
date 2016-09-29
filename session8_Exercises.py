# Exercise 4_1

def price(x):
    count = 0
    for letter in x:
        count += ord(letter)-96
    return count

# print('bananas ', '$',price('bananas'))
# print('rice ', '$', price('rice'))
# print('paprika ', '$', price('paprika'))
# print('potato chips ', '$', price('potato chips'))
# print('-------------------------') # 25
# print('Total ', '$', price('bananas')+price('rice')+price('paprika')+price('potato chips'))


# Exercise 4_2

print('{:18} {:1} {:6}'.format('bananas', '$', '52.00'))
print('{:18} {:1} {:6}'.format('rice', '$', '35.00'))
print('{:18} {:1} {:6}'.format('paprika', '$', '72.00'))
print('{:18} {:1} {:6}'.format('potato chips', '$', '78.00'))
print('--------------------------') # 26
print('{:17} {:1} {:6}'.format('Total', '$', '237.00'))

# Exercise 4_3

print('{:14} {:1} {:6}'.format('bananas', '$', '52.00'))
print('{:14} {:1} {:6}'.format('rice', '$', '35.00'))
print('{:14} {:1} {:6}'.format('paprika', '$', '72.00'))
print('----------------------') # 22
print('{:13} {:1} {:6}'.format('Total', '$', '237.00'))

# Exercise 5

def any_lowercase1(s):       # check only the first letter whether it is lower or capital
    for c in s:
        if c.islower():
            return True
        else:
            return False
        
def any_lowercase2(s):       # Returns true no matter what letters you type in 
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):       # Returns False if the last letter is not lowercase.
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):       # Returns True if there is any lowercase letter in the string.
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):       # Returns False if any uppercase letter is in the string.
    for c in s:
        if not c.islower():
            return False
    return True

# Exercise 6

def rotate_word(s, x):
    result = str()
    for letter in s:
        y = ord(letter) + x
        if y > 122 :
            result += chr(y-26)
        else:
            result += chr(y)
    return result

input()