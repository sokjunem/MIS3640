
team = 'New England Patriots'
print(team[0])
# Print(team[1.5]) : do not use floating number. error
print(len(team))

print(team[19])

index = 0
while index < len(team):
    letter = team[index]
    print(letter)
    index += 2


for letter in team:
    print(letter)


# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
# for letter in prefixes:
#     if letter == 'O' or letter == 'Q' :
#         suffix = 'uack'
#     else:
#         suffix = 'ack'
#     print(letter + suffix)

print(team[0:11]) # = team[:11]
print(team[12:20]) # = team[12:]

print(team[::2])
print(team[1::2])