from random import randint
import sys

pick = randint(1, 100)

tryout_str=raw_input("Your guess?")
if tryout_str!=int():
    print "A number, FREAK!"
    print "Go back to school!"
    sys.exit()
tryout=int(tryout_str)
while tryout != pick:
    if tryout > pick:
        print "Your guess is too high."
    elif tryout < pick:
        print "Your guess is too low."
    tryout_str=raw_input("Your guess?")
    tryout=int(tryout_str)
    
print "well done! What a brain!"
