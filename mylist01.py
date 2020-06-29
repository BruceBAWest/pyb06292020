#!/usr/bin/python3
'''
Author: Bruce West
purpose of this program is learning python lists.
'''

# all code should live inside of a function
def main():
    movies = []   # one way to create a list 
    movies.append("Avatar") # .append is a list method that applies the value
                            # passed to it at the END of the list

    movies.append("Back to the Future")

    print(movies) # use the print FUNCTION to display to std out
    
    movies.append("Ghostbusters") #add ghostbusters to end of list

    # ["Avatar", "Back to the Future", "Ghostbusters"]
    print(movies[2]) # pring ghostbusters
    print(movies[-1]) #print out ghostbusters

    print(movies.index("Ghostbusters")) # print out the index of first ghostbusters instance

if __name__ == "__main__":
    main()
