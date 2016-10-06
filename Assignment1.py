# Assignment 1_1 #####################################

def factor(a):
    print('the prime factors for', a, 'are:')
    undivisable_factors = []
    i = 2
    while a > 1:
        if a % i == 0:
            a = a / i
            undivisable_factors.append(i)
        else:
            i += 1
    return undivisable_factors
    
print(factor(40))
'''
need to obtain prime factors. i starts from 2 in order to exclude 1
append allows i to accumulate answers in ()
'''

# Assignment 1_2 ######################################

def isPalindrome(word):

    if len(word) <= 1:
        print('That\'s a palindrome')
    else:
        while word[0] == word[-1]:
            return isPalindrome(word[1:-1])
        print('That isn\' a palindrome.')
'''
Through recursive function, eliminate the letters(if they are identical) 
from the edge.import
len(word) is limited to 1 or less because if pairs even out, there will be no 
remaining letter. If the length of the word is odd number, one letter lefts
at the end.
'''
print(isPalindrome('rotor'))

# Assignment 1_3 #######################################

import random

def drunkard_walk(a, b, number):
    start = (0, 0)
    for i in range(0, number):
        decision = random.choice([(a,0),(-a,0),(0,b),(0,-b)])
        start = tuple(map(sum,zip(decision, start)))         # allows tuple to add up
        
    print("The drunkard started from (%d,%d)." % (0, 0))
    
    print(" After", number, "intersections, he's",start, "blocks from where he started.")

drunkard_walk(10, 10, 5)
'''
number for a is distance you move for x-axis. number for y is distance you move for
y-axis. number includes the decision you choose from the starting point. In the for
loop, decision generates where to go(distance written for a and b) every round. 
start ables each decision made to add up. As a result, we can see how much to x-axis
and y-axis you moved from the original point(0, 0)
'''

# Assignment 1_4 ###################################

from random import randint
from math import log

# Define constant variables.
HUMAN = 0
COMPUTER = 1
SMART = 0
DUMB = 1

# Create the initial pile, determine the starting player and the computer's
# strategy.
pile = randint(10, 100)
turn = randint(0, 1)
strategy = randint(0, 1)


def nim():
    turn = randint(0, 1)
    strategy = randint(0, 1)
    pile = randint(10, 100)
    print("Total number of pile is ", pile, ". Turn starts with ", turn, ". Computer level is in ", strategy, ' mode.')
    """
    return True if the winner is human, False if winner is computer.
    """
    # While the game is still being played.
    while pile > 1:
        take = randint(1, int(pile/2))
        if turn == COMPUTER:
            if pile == 1:
                take == 1
                
                # Take the last marble.
                
            elif strategy == DUMB:
                    take = randint(1, int(pile/2))
                    
                # Take a random, legal number of marbles from the pile.
                
            elif pile == 3 or pile == 7 or pile == 15 or pile == 31 or pile == 63:
                take = randint(1, int(pile/2))
                
                # The computer is smart, but can't make a smart move.
                # Take a random, legal number of marbles from the pile.
                
            else:
                if pile > 63:
                    n = 6
                elif pile > 31:
                    n = 5
                elif pile > 15:
                    n = 4
                elif pile > 7:
                    n = 3
                elif pile > 3:
                    n = 2
                else:
                    n = 1
                take = pile + 1 - (2**n)
                    
                    
                # The computer is smart and can make a smart move.
                # Take marbles so that the pile will be be a power of 2, minus
                # 1.
                
            # Update pile
            pile -= take
            print("The computer took %d marbles, leaving %d.\n" % (take, pile))
            # take is the variable you might need above
            turn = HUMAN

        elif turn == HUMAN:
            print("Your turn.   The pile currently has", pile, "marbles in it.")

            take = int(input("How many marbles will you take? "))
            # Force the user to take a legal number of marbles.
            if pile > 1 :
                if take > (pile/2):
                    print("That is not a legal number of marbles. Please pick the number again.")
                    continue
                else :
                    pile -= take

            # Update pile
            else:
                print("you only have one marble to take. ")
                take == 1
                pile -= take
            print("Now the pile has", pile, "marbles in it.\n")
            turn = COMPUTER

    return turn == COMPUTER

if nim():
    print("You Won!")
else:
    print("The computer won!")
'''
play on computer side is categorized by the hierarchy of the order. Also the setting the limit for the take in the beginning
prevent computer to pick negative variable during the game.
'''

# Assignment 1_5 (optional) #############################
import turtle
import random
sj = turtle.Turtle


def north(x):
    turtle.lt(90)
    turtle.fd(x)
    turtle.setheading(0)

def west(x):
    turtle.lt(180)
    turtle.fd(x)
    turtle.setheading(0)

def south(x):
    turtle.lt(270)
    turtle.fd(x)
    turtle.setheading(0)

def east(x):
    turtle.fd(x)
    turtle.setheading(0)
    
def drunkard_map(distance, intersection):
    for i in range(intersection):
        decision = random.choice([1, 2, 3, 4])
        print(decision)
        if decision == 1:
            north(distance)
        elif decision == 2:
            west(distance)
        elif decision == 3:
            south(distance)
        else:
            east(distance)

drunkard_map(50, 5)

input()