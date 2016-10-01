# Assignment 1_1

# def factor(a):
#     print('the prime factors for', a, 'are:')
#     undivisable_factors = []
#     i = 2
#     while a > 1:
#         if a % i == 0:
#             a = a / i
#             undivisable_factors.append(i)
#         else:
#             i += 1
#     return undivisable_factors
    
# print(factor(40))
'''
need to obtain prime factors. i starts from 2 in order to exclude 1
append allows i to accumulate answers in ()
'''

# Assignment 1_2

def isPalindrome(word):
    if len(word) <= 1:
        return True
    else:
        while word[0] == word[-1]:
            return isPalindrome(word[1:-1])
        
'''
Through recursive function, eliminate the letters(if they are identical) 
from the edge.import
len(word) is limited to 1 or less because if pairs even out, there will be no 
remaining letter. If the length of the word is odd number, one letter lefts
at the end.
'''
print(isPalindrome('rotor'))

