#!/usr/bin/env python3
'''
Author: bruce west
just mucking about with this here python3
'''
# i legit have no clue what I'm doing
# i gather I'm supposed to be retrieving data 
# from some api... Idk
# ok, ok. retrieve location data from http://api.open-notify.org/iss-now.json
# and display it in some way
# in such case, I need to install a request library

import requests

# create a main function to house the below in
# requests.get('http://api.open-notify.org/iss-now.json')

def main():
    webdata = requests.get('http://api.open-notify.org/iss-now.json')
    
    print("Where is the ISS at now?")

    for data in webdata.json():
        print(data)
        # print(webdata.json()[data])

    issdata = webdata.json()

    print("Longitude: ", issdata["iss_position"]["longitude"])
    
    print("Latitude: ", issdata["iss_position"]["latitude"])

if __name__ == "__main__":
    main()

