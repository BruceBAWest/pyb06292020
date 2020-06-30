#!/usr/bin/python3
'''
Author: bruce west
this program harvests SpaceX data avil from https://api.spacexdata.com/v3/cores#
using the Python Standard Library methods
'''

import urllib.request
import json

# global constant of the api we want to work with
SPACEXURI = "https://api.spacexdata.com/v3/cores#"

#main for api request
def main():
    # create a urllib.request response object by sending an HTTP GET to SPACEXURI
    coreData = urllib.request.urlopen(SPACEXURI)

    # pull STRING data off of the 200 response (even though its JSON)
    xString = coreData.read().decode()
    print(type(xString))
    
    # convert STRING data into Python lists and dicts
    listOfCores = json.loads(xString)
    print(type(listOfCores))

    for core in listOfCores:
        print(core, end="\n\n")

if __name__ == "__main__":
    main()
