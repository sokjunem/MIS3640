# [10, 20, 30, 40]
# ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']

# # The elements of a list don’t have to be the same type. 
# # A list within another list is nested. 
# ['spam', 2.0, 5, [10, 20]] 


# AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
# numbers = [42, 123]
# empty = []
# print(AFC_east, numbers, empty)

# AFC_east[3] = 'New York Giants'
# print(AFC_east)

# AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
# print('Buffalo Bills' in AFC_east)

# for team in AFC_east:
#     print(team)

numbers = [2, 0, 1, 6, 9]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
    
print(numbers)
print(len(numbers))

# my_list = ['spam', 1, ['New England Patriots', \
#                        'Buffalo Bills', 'Miami Dolphins', \
#                        'New York Giants'], \
#            [1, 2, 3]]
# print(len(my_list))

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(c)

# [0] * 4
# ['Tom Brady', 'Bill Belichick']*3

# t = ['a', 'b', 'c', 'd', 'e', 'f']
# t[1:3] = ['x', 'y']
# print(t)
# print(t[1:3])

# def capitalize_all(t):
#     res = []
#     for s in t:
#         res.append(s.capitalize())
#     return res

# t = [1, 2, 3]
# print(sum(t))

# print(capitalize_all('hi, nice to meet you'))

def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res

print(only_upper('ABCED'))

t = ['a', 'b', 'c', 'd']
x = t.pop(1)
# pop modifies the list and returns 
# the element that was removed. 
print(x)
print(t)

x = t.pop()
# If you don’t provide an index, 
# it deletes and returns the last element.
print(x)
print(t)

t = ['a', 'b', 'c', 'd', 'e']
del t[1:3]
print(t)

team = 'Patriots'
t = list(team)
print(t)

team = 'New England Patriots'
t = team.split()
print(t)

s = 'spam-spam-spam'
delimiter = '-'
t = s.split(delimiter)
print(t)

t = ['New', 'England', 'Patriots']
team = ' '.join(t)
print(team)

input()