#!/usr/bin/python3
"""
Author: RZFeeser
This program harvests SpaceX data avail from https://api.spacexdata.com/v3/cores using the Python Standard Library methods
"""

# using std library method for getting at API data
import requests

# GOBAL / CONSTANT of the API we want to lookup
SPACEXURI = "https://api.spacexdata.com/v3/cores"

def main():
    # create requests response object by sending an HTTP GET to SPACEXURI
    coreData = requests.get(SPACEXURI)

    # pull json off 200 and convert to lists and dicts
    listOfCores = coreData.json()

    for core in listOfCores:
        print(core, end="\n\n")


if __name__ == "__main__":
    main()
