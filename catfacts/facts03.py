#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests
import random

def main():
    """Run time code"""
    ## create r, which is our request object
    r = requests.get('https://cat-fact.herokuapp.com/facts')

    ## catfact is our iterable -- that just means it will take on the values found within
    ## r.json()["all"], one after the next-- which happens to be a dictionary
    ## the code within the loop, says, "from that single dictionary
    ## print the value associated with text"
#    for catfact in r.json()["all"]:
#        print(catfact.get("text"))  # the .get() method returns NONE if key not found
    
    # strip json off 200 response
    listofcatfacts = r.json()

    # select single dict from list of dictionaries 
    randomfact = random.choice(listofcatfacts["all"]) 

    #print the value assoc w/ key text from single dict
    print(randomfact["text"])

    # this one line, uncommented, would do same as aboce 3
    # print(random.choice(r.json()["all"])["text"])

    print(r.status_code)

main()

