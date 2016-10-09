[10, 20, 30, 40]
['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']

# The elements of a list don’t have to be the same type. 
# A list within another list is nested. 
['spam', 2.0, 5, [10, 20]] 


AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
numbers = [42, 123]
empty = []
print(AFC_east, numbers, empty)

AFC_east[3] = 'New York Giants'
print(AFC_east)

AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
print('Buffalo Bills' in AFC_east)

for team in AFC_east:
    print(team)

numbers = [2, 0, 1, 6, 9]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
    
print(numbers)

my_list = ['spam', 1, ['New England Patriots', \
                       'Buffalo Bills', 'Miami Dolphins', \
                       'New York Giants'], \
           [1, 2, 3]]
print(len(my_list))

input()