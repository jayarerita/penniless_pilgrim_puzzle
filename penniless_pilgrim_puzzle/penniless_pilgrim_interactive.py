# This is a simple interactive version of the penniless pilgrim math puzzle. 

import pilgrim

# Now the game begins...

print("You are a traveler starting at the northwest corner of the grid below.")

# new instance of traveler
me = pilgrim()

me.print_grid()
print("You can go : " + str(me.valid_dir()))
print("Please select a direction to move: ")
direction = input()
# Send the direction input to the move method, but make sure it is uppercase first.
me.move(direction.upper())

# As long as you can still move continue to update the grid, show options, and accept directions
while me.valid_dir() != [] or location != [4, 0]:
    me.print_grid()
    print("history" + str(me.history))
    print("Your current tax is: " + str(me.tax))
    print("You can go : " + str(me.valid_dir()))
    print("Please select a direction to move: ")
    direction = input().upper()
    me.move(direction)

# Once there are no more options to move or you have arrived at the temple print last grid and summary.
me.print_grid()
print("You can no longer move.")
print("Your current tax is: " + str(me.tax))