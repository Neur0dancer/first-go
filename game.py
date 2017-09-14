from random import randint
import sys

rules=raw_input("Do you want to know the rules?(y/n)")
explanation=rules.lower()
if explanation=="y":
    print "I will pick a number between 1 and 100 (included)."
    print "Your job is to find it."
elif explanation!="y" and explanation != "n" :
    print "Y for yes, N for no!"
    print "What's so difficult about that?"
    print "Go back to school, DUMBASS!"
    sys.exit()

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

