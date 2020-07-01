#!/usr/bin/python3
'''
jeopardy game
'''

# import a lib to make an http request
import requests

def main():
    # prompt for initials
    player = input("Type in your initals: ")
    rounds = input("How many rounds would you like to play? ")
    playerscore = 0 # counter for the player score

    # make a req to http://jservice.io/api/random
    zresp = requests.get(f"http://jservice.io/api/random?count={rounds}")

    # strip off json from 200 response
    listofquestions = zresp.json()

    # run the game by loopoing over the results
    for jquestion in listofquestions:
        # each time through loop, pose Q to player
        print(f"Alex says: {jquestion['question']}")
        playeranswer = input(f"\tType your Answer --> ")
        
        # user can respond by typing input (normalize to lowercase) 
        if playeranswer.lower() == jquestion['answer'].lower():
            print(f"Alex says: That's right, you add {jquestion['value']} to your score")
            # alter playerscore counter, increase by the question's point value
            playerscore = playerscore + jquestion['value']
        else: 
            print(f"Alesx says:Not quite right? The answer were were looking for was {jquestion['answer']}")

    # after 10 rounds, show the player's score
    print(f"Alex says: Let's see how you did.\nLooks like your score is {playerscore}")

    # if their score is higher than and of those in highscore.txt, ask for then write palyer's intials, and their score, to highscore.txt
    with open("jeopardyhighscores.txt") as jhs:
        highscorelist = jhs.readlines()

    # sore the data taken from the file
    highscorelist.sort()

    for score in highscorelist:
        if playerscore > int(score.rstrip("\n")):
            print("looks like a high score")
            highscorelist.remove(score)
            highscorelist.append(str(playerscore))
            break

    with open("jeopardyhighscores.txt", "w") as jhs:
        for score in highscorelist:
            jhs.write(score.rstrip("\n")+"\n")

if __name__ == "__main__":
    main()

 
