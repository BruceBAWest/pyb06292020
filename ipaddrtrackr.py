#!/usr/bin/python3
'''
Author: Bruce West
this creepy script tracks where in the world an ip addr is at
'''
#imports section
import argparse
import requests


#mission: find location of entered ip
def main():

    if args.ip:
        ipToLookUp = args.ip
    else: 
        ipToLookUp = input("What is the IP address to lookup?")

    zresp = requests.get(f'http://ip-api.com/json/{ipToLookUp}') # sends an HTTP GET
    print(zresp.json()) # print out the json attached to the response zresp 

# only true is you run the script directoly (ie python3 ipaddrtrackr.py) 
if __name__ == "__main__":
    parser = argparse.ArgumentParser() # short descript avail via help flag --help or -h
    parser.add_argument("--ip", help="The IP address to lookup via the API service")
    
    args = parser.parse_args()
    main()
