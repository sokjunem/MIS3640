'''
# Exercise 1
result = 0
for i in range(1, 11, 2):
    print('current i: ', i)
    result = result + i # += means result = result + i. result += i = [result = result + i]
print(result)

result = 0
for i in range(11):
    if i % 2 == 1:
        print ('current i: ', i)
        result += 1

print(result)

def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print ('Blastoff!')

countdown(5)

iteration = 0
count = 0
while iteration < 5:
    count+=12
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration =+ 1


while True:
    line = input('>')
    if line == 'done':
        break
    print(line)

print('Done!')

result = 0
i = 1
while i < 11:
    result = result + i
    i = i + 1
print(result);
'''
mysum = 0
for i in range(5, 11, 2):
    mysum += i
    if mysum == 5:
        break
print(mysum)

input()