from random import randint

rules=raw_input("Do you want to know the rules?(y/n)")
explanation=rules.lower()
if explanation=="y":
    print "I will pick a number between 1 and 100 (included)."
    print "Your job is to find it."

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

