#!/usr/bin/env python3
'''
Author: Bruce West
program checks hostname
'''

##collect input from user 
hostname = input("What value should we set for hostname?")

## here we use the str.lower() method to return a lowercase string
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("hostname matches expected config")

## Always print out to the user
print("Exiting the script")

