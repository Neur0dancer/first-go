from random import randint
pick = randint(1, 100)
count=1
tryout_str=raw_input("Your guess?")
tryout=int(tryout_str)

while tryout != pick:
    if tryout > pick:
        print "Your guess is too high."
    elif tryout < pick:
        print "Your guess is too low."
    tryout_str=raw_input("Your guess?")
    tryout=int(tryout_str)
    count+=1

print "well done! What a brain!"
print "You've done it in %s attempts" %(count)
