import os

# This class will hold current and accumulated information on a pilgrim.
class pilgrim(object):

    #Create the attributes of the class
    def __init__(self):
        self.loc = [0,4]    # The coordinates of the pilgrim as a string.
        self.tax = 0.0        # The accumulated tax of the pilgrim.
        self.history = []   # The history of streets traveled.
    
    # Add a street traveled to the history of the pilgrim.
    def add_street(self, street):
        self.history.append(street)

    # Check to see if a street has been traveled in one direction or the other.
    # Returns True if it has been traveled before or False if it has not.
    def search_street(self, street):
        traveled = False    # False indicates the street has not been traveled. Start at False.
        # Create the reverse string of the street to check also incase it was traveled in the 
        # opposite direction.
        street_rev = street.split(" to ")[-1] + ' to ' + street.split(" to ")[0]

        # Check all previously traveled streets in history
        for old in self.history:
            # Check to see if equal to the current direction or the reverse.
            if old == street or old == street_rev:
                traveled = True

        return traveled

    # Check to see if the current locaion is along any borders of the town. If so
    # remove the possible direction out of town.
    def out_of_bounds(self, loc):
        # Create empty list assing no directions are out of bounds to start
        out_of_bounds_streets = []

        # Check the X coord to see if it is on the western board, if so add 'W'
        if loc[0] == 0:
            out_of_bounds_streets.append('W')
        # Check the X coord to see if it is on the western board, if so add 'E'
        if loc[0] == 4:
            out_of_bounds_streets.append('E')
        # Check the Y coord to see if it is on the western board, if so add 'N'
        if loc[1] == 4:
            out_of_bounds_streets.append('N')
        # Check the Y coord to see if it is on the western board, if so add 'S'
        if loc[1] == 0:
            out_of_bounds_streets.append('S')

        return out_of_bounds_streets

    # Given any loc as a list of two integers between 0 & 4 specifying a locatoin on the 5x5 node 
    # grid and given a list of streets already traveled this function will return a list of valid 
    # directoins to travel.
    def valid_dir(self):
        # Create an empty list of valid directions.
        valid = []
        # get dictionary of streets in all directions based on current location
        possible_streets = self.direction_streets()
        # Set all the forbidden streets (ie - those walked on before) to False
        forbidden_streets = {'N':False, 'S':False, 'E':False, 'W':False}
     
        # Check all directions, N, S, E, W
        for key in possible_streets:
            # Send the street to search_street method and if True change value in
            # the forbidden streets dictionary to True
            if self.search_street(possible_streets[key]):
                forbidden_streets[key] = True

        # add all the not forbidden directions to the list of valid directions
        for key in forbidden_streets:
            if forbidden_streets[key] == False:
                valid.append(key)

        # Subtract any directions out of bounds from the valid directoins
        #### Can't subtract need to do something else
        temp = valid
        valid = [x for x in temp if x not in self.out_of_bounds(self.loc)]

        # Return a list of possible directions to move
        return(valid)

    # Returns a dictionary of all the directoins  paired with the consequential street strings 
    # if that direction is traveled.
    def direction_streets(self):
        # Create a series of strings representing the a street to travel. 
        street_N = str(self.loc) + ' to ' + str([self.loc[0], self.loc[1]+1])
        street_S = str(self.loc) + ' to ' + str([self.loc[0], self.loc[1]-1])
        street_E = str(self.loc) + ' to ' + str([self.loc[0]+1, self.loc[1]])
        street_W = str(self.loc) + ' to ' + str([self.loc[0]-1, self.loc[1]])
        streets = {'N':street_N, 'S':street_S, 'E':street_E, 'W':street_W}

        return streets

    # Add tax to the running total based on direction moved
    def add_tax(self, dir):
        
        if dir == 'S':
            self.tax = 2 * self.tax
        if dir == 'N':
            self.tax = self.tax / 2
        if dir == 'E':
            self.tax += 2
        if dir == 'W':
            self.tax -= 2

    # Change the location coordinates based on direction moved
    def new_loc(self, dir):
        if dir == 'N':
            self.loc[1] += 1
        if dir == 'S':
            self.loc[1] -= 1
        if dir == 'E':
            self.loc[0] += 1
        if dir == 'W':
            self.loc[0] -= 1

    def move(self, dir):
        dir = dir.upper()
        dir_list = ['N', 'S', 'E', 'W']
        if dir not in dir_list:
            print("You entered an invalid character")
        else:
            # Get list of possible streets to take in all directions
            possible_streets = self.direction_streets()
            # Add the chosen street to the history of traveled streets
            self.add_street(possible_streets[dir])
            # Update the tax
            self.add_tax(dir)
            # Update the current location
            self.new_loc(dir)

    # clear the text print out and print a new grid showing the current location
    def print_grid(self):
        # clear text print out
        os.system('cls')
        for y in range(4, -1, -1):
            line = ''
            for x in range(5):
                # when the current location is encounted replace numbers
                if x == self.loc[0] and y == self.loc[1]:
                    section = '(XX)'
                else:
                    section = '('+str(x)+str(y)+')'
                if x != 4:
                    section += '-'
                line += section
            print(line)
            # Verical street representations everyother line
            if y != 0:
                print(' |     |    |    |    |')

    # this method will move the travler from 0,4 to 2,4 as stated in the problem start by moving E twice
    def modified_start(self):
        self.move('E')
        self.move('E')

    # reset the pilgrim to the starting location 0,4 and clear all tax and history
    def reset(self):
        self.loc = [0,4]    # The coordinates of the pilgrim as a string.
        self.tax = 0.0        # The accumulated tax of the pilgrim.
        self.history = []   # The history of streets traveled.


