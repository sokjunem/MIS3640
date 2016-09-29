"""
Question 1:
"""


def crazy_about_9(a, b):
    if a == 9 or b == 9 :
        return True
    if a + b == 9 :
        return True
    if abs(a-b) == 9 :
        return True
    else:
        return False
 

# When you've completed your function, uncomment the
# following lines and run this file to test!

print(crazy_about_9(2, 9))
print(crazy_about_9(4, 5))
print(crazy_about_9(3, 8))


"""
-----------------------------------------------------------------------
Question 2:
A year with 366 days is called a leap year. Leap years are necessary to
keep the calendar synchronized with the sun because the earth revolves
around the sun once every 365.25 days. Actually, that fgure is not
entirely precise, and for all dates after 1582 the Gregorian correction
applies. Usually years that are divisible by 4 are leap years, for
example 1996. However, years that are divisible by 100 (for example,
1900) are not leap years, but years that are divisible by 400 are leap
years (for example, 2000). 
"""


def leap_year(year):
    if year%400 == 0:
        return True
    if year%100 == 0:
        return False
    if year%4 == 0:
        return True
    else:
        return False
    """
    year(int): a year
    Returns True if year is a leap_year, False if year is not a leap_year. 
    """
    pass

# When you've completed your function, uncomment the
# following lines and run this file to test!

print(leap_year(1900))
print(leap_year(2016))
print(leap_year(2017))
print(leap_year(2000))


"""
-----------------------------------------------------------------------
Question 3:
Write a function with loops that computes The sum of all squares between 
1 and n (inclusive).
"""


def sum_squares(n):
   '''
    if n > 1:
        for i in range(1,n)
        (n**2) + ((n-1)**2)
    if n == 1
        return 1
    '''  
# correct
    result = 0   # indicate starting from 0....??
    for x in range(1, n+1):
        result += n * n
    return result

# When you've completed your function, uncomment the
# following lines and run this file to test!

print(sum_squares(3))
# print(sum_squares(100))
    