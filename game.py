from random import randint
import sys
pick = randint(1, 100)

tryout_str=raw_input("Your guess?")
tryout=int(tryout_str)

while tryout != pick:
    if tryout<1 or tryout>100:
        print "Between 1 and 100"
        print "learn to count and come back, JERK!"
        sys.exit()
    elif tryout > pick:
        print "Your guess is too high."
    elif tryout < pick:
        print "Your guess is too low."
    tryout_str=raw_input("Your guess?")
    tryout=int(tryout_str)
    
    
print "well done! What a brain!"
