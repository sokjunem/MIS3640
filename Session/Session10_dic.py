# names = ['Rose', 'Jerry', 'Alex']
# scores = [95, 75, 85]
# i = names.index('Jerry')
# print(scores[i])

# print(scores[names.index('Jerry')])

# grades = {'Jerry': 75, 'Rose': 95}
# print(grades['Jerry'])

# grades['Brian'] = 90
# print(grades)

# print(len(grades))
# print('Jerry' in grades)
# print(90 in grades.values())

def histogram(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
# print(histogram('bookkeeper'))

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse
hist = histogram('parrot')
print(hist)
inverse = invert_dict(hist)
print(inverse)