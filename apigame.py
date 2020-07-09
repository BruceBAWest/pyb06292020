#!/usr/bin/python3
'''
Author: Bruce West
trying to make an api-based g&a game
'''
# imports section
import requests

def main():
    counter = 0
    base_URI = 'http://jservice.io/'
    rand = requests.get(f'{base_URI}/api/random?count=10')
    random_Q = rand.json()

    for q in range(10):
        print(random_Q[q]['answer'])
        answer = str(input(random_Q[q]["question"] + "\n"))
        if answer.lower() == random_Q[q]["answer"].lower():
            print("correct!")
            counter += 1
        else:
            print("That's not it")
    print(counter)

if __name__ == "__main__":
    main()

