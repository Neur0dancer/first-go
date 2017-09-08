from random import randint
pick = randint(1, 100)

tryout_str=raw_input("Your guess?")
tryout=int(tryout_str)

while tryout != pick:
    if tryout > pick:
        print "Your guess is too high."
    elif tryout < pick:
        print "Your guess is too low."
    tryout_str=raw_input("Your guess?")
    tryout=int(tryout_str)
    
print "well done! What a brain!"
