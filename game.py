from random import randint
pick = randint(1, 100)
return pick
#print pick

tryout=raw_input("Your guess?")
int(tryout)
while tryout != pick:
    if tryout > pick:
        print "Your guess is too high."
    elif tryout < pick:
        print "Your guess is too low."
    tryout=raw_input("Your guess?")
    int(tryout)
    
if tryout == pick:
        print "well done! What a brain!"
