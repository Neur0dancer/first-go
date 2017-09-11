from random import randint
pick = randint(1, 100)
count=0
tryout=int(tryout_str=raw_input("Your guess?"))

while tryout != pick:
    if tryout > pick:
        print "Your guess is too high."
    elif tryout < pick:
        print "Your guess is too low."
    tryout=int(tryout_str=raw_input("Your guess?"))
    count+=1

print "well done! What a brain!"
print count
