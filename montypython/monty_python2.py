#!/usr/bin/env python3
'''
Author: Bruce West
if, elif in python
'''

# counter
round = 0

# create a while loop that loops forever
while True:
    #print round counter 
    round = round + 1
    #print challenge
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
    #get answers
    answer = input("Your guess--> ")
    #check if answer correct
    if answer == 'Brian':
        # print if correct
        print('Correct')
        #leave loop if correct
        break
    #if three rounds fail
    elif round==3:
        #print sorry
        print("Sorry, the answer was Brian.")
        #break loop
        break
    else: 
        print("Sorry! Try again!")





