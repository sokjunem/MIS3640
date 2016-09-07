# Class 1 Exercise 2
print((42*60)+42)
print(10/1.61)
print(((42*60)+42)/(10/1.61))
print((10/1.61)/(((42*60)+42)/3600))

# Class 2 Exercise 1_1

message = 'Please enter the r'
print(message)
r = int(input()) # allow integer to be entered for input()
π = 3.14159
v = ((4/3)*π*r**3)
message = 'The volume of a sphere is %.2f' % v
print(message)

# Class 2 Exercise 1_2

message = 'How many copies do you want?'
print(message)
copy = int(input())
Price = 24.95
Discount = Price * 0.6
Shippingcost = 3 + 0.75 * (copy - 1)
totalcost = Discount * copy + Shippingcost
message = 'The total cost is %.2f' % totalcost
print(message)

# Class 2 Exercise 1_3

pace1 = 2*(8+(15/60))
pace2 = 3*(7+(12/60))
time = pace1 + pace2
minute = time + 52 - 60
hour = 6 + 1
message = 'You will return by %2d : %02d' % (hour, minute)
print(message)

# Class 2 Exercise 1_4

message = 'What is your first grade?'
print(message)
score = int(input())
message = 'What is your last grade?'
print(message)
score2 = int(input())
improve = ((score2 / score) - 1) * 100
message = 'You have improved %.1f %% so far' % improve
print(message)

input()