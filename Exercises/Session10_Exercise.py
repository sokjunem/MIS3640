# def histogram(s):
#     d = {}
#     for c in s:
#         if c not in d:
#             d[c] = 1
#         else:
#             d[c] += 1
#     return d
# print(histogram('bookkeeper'))

#Exercise 1
def histogram(s):
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

print(histogram('bookkeeper'))

def print_hist(h):
    for c in sorted(h):
        print(c, h[c])
print_hist(histogram('bookkeeper'))

