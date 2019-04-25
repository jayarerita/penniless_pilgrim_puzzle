'''
A pilgrim arrives in Duona, a sixteen-block town created by five 
streets running north-south that intersect with five streets running
east-west. Like all pilgrims, she arrives in the northwest corner of 
town, and needs to make her way to a shrine in the southeast corner. 
Unfortunately for the pilgrim, Duona imposes a tax system on visitors, 
charging 2 silver pieces for each block walked to the east, and 
doubling what you owe every time you walk south. To make the payment 
system fairer and encourage longer stays, they subtract 2 silver pieces 
for each block walked to the west, and halve what you owe when you walk
a block north. The townsfolk keep track of your path, and you must pay 
in full on your arrival in the southeast corner. (Legend has it that certain 
savvy travelers have planned trips through the town and ended up receiving 
silver by following the tax rules.) As a central tenant of her pilgrimage 
she cannot travel the same stretch of ground twice.

The pilgrim has no money, and has no intention of leaving with any. 
How can she travel to the southeast corner of Duona without owing or 
receiving any silver?

Summary of directions:
North: x / 2
South: x * 2
East: x + 2
West: x - 2

Credit: The NYTimes' Daniel Finkel
https://wordplay.blogs.nytimes.com/2013/08/26/pilgrim/
'''

import pandas as pd

# Given any loc as a list of two integers between 0 & 4 specifying a locatoin on the 5x5 node 
# grid and given a list of streets already traveled this function will return a list of valid 
# directoins to travel.
def valid_dir(loc, history):
    # Create an empty list of valid directions.
    valid = []
    # Create a series of strings representing the a street to travel. 
    ### Need to come up with a way to deal with reverse directions.
    street_N = str(loc) + 'to' + str([loc[0], loc[1]+1])
    street_S = str(loc) + 'to' + str([loc[0], loc[1]-1])
    street_E = str(loc) + 'to' + str([loc[0]+1, loc[1]])
    street_W = str(loc) + 'to' + str([loc[0]-1, loc[1]])
    possible_streets = {'N':street_N, 'S':street_S, 'E':street_E, 'W':street_W}
    # Set all the forbidden streets (ie - those walked on before) to False
    forbidden_steets = {'N':False, 'S':False, 'E':False, 'W':False}
    # Iterate through all rows in the df of the traveler's history and see if they have 
    # traveled the street before.
    for row in history:
        # Iterate through all the possible directoins of travel
        for key in possible_streets:
            # If the street has been traveled before, change its value in the 
            # forbidden_streets dictionary to True
            if possible_streets[key] == history.loc[row]:
                forbidden_steets[key] = True

    # add all the not forbidden directions to the list of valid directions
    for key in forbidden_streets:
        if forbidden_steets[key] == Fallse:
            valid.append(key)

    # Check to see if the current locaion is along any borders of the town. If so
    # remove the possible direction out of town.
    if loc[0] == 0:
        valid.remove('W')
    if loc[0] == 4:
        valid.remove('E')
    if loc[1] == 4:
        valid.remove('N')
    if loc[1] == 0:
        valid.remove('S')

    # Return a list of possible directions to move
    return(valid)


### Should probably create a traveler class to hold attributes such as current location 
#(a list of 2 integer coordinates), historical streets (a list of all the streets traveled), 
# tax owed (a float indicated accrued tax up to that point)
traveler = pd.DataFrame([0, 0, null], columns = ['x', 'y', 'hist_streets'])

# All possible, though maybe not valid, directions of travel from any point
directions = ['N', 'S', 'E', 'W']

for dir in directions:
    valid = valid_dir(dir)



