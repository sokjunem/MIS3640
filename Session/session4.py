

# Add new functions
def print_lyrics():
    print("Hey Jude. Don't make it bad.")
    print("Take a sad song and make it better.")

#print(type(print_lyrics))
#print_lyrics()

def repeat_lyrics():
    print_lyrics()
    print("na na na na na na na na na")
    print_lyrics()

#repeat_lyrics()

def print_twice(a):
    print(a)
    print(a)

print_twice('Babson')

my_name = "SJ"
print_twice(my_name)

def my_abs(n):
    if n >= 0:
        print(n)
    else:
        print(-n)

my_abs(5)
my_abs(-234)

def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)

line1 = 'Bing tiddle '
line2 = 'tiddle bang.'
#cat_twice(line1, line2)

#print(cat)
#print(line1)

def give_me_a_break():
    str1 = 'break'
    print('another break')
    return str1
    
new_str = give_me_a_break()

print(new_str)
#new_str

#give_me_a_break()

#print(give_me_a_break())

def a_new_function_demo():
    s = 0
    for x in 'Chris':
        print(x)
        print(ord(x))
        s = s + ord(x)
    return s

a_new_function_demo()

def my_abs(n):
    if isinstance(n, int) or isinstance(n, float):

        if n >= 0:
            return(n)
        else:
            return(-n)
    else:
        print('invalid value')

print(my_abs('8'))

print(my_abs(109))

print(my_abs(-24))



input()