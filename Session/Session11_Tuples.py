def sumall(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result

print(sumall(1,2,3,4,5,6))