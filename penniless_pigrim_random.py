import pilgrim
import random

# Now the game begins...

me = pilgrim()

me.modified_start()

# Until the bottom corner is reached with 0 tax continue to move randomly
counter = 1
while not(me.tax <= 0 and me.loc == [4,0]):
    # As long as there is a direction to move, pick a random one an move
    if not (me.valid_dir() == []):
        index = random.randint(0, len(me.valid_dir())-1)
        #print("valid_dir: %s len(valid_dir): %i index: %i" % (str(me.valid_dir()), len(me.valid_dir()), index))
        rand_dir = me.valid_dir()[index]
        #print("rand_dir: %s" % (rand_dir))
        me.move(rand_dir)
    else:
        me.reset()
        me.modified_start()
        counter += 1

print("counter: %i" % counter)
print("Your current tax is: " + str(me.tax))
print("Your current location is: " + str(me.loc))
print(me.history)
    