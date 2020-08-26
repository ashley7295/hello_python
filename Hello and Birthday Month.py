
# variables & inputs
name = (input("please enter your name:"))

month = (input("please enter the month you were born:"))

# actions to inputs
print ("Hello " + name + "!")

# counting letters in the string
print ("you have this many letters in your name: ")
print(len(name))


#i was born in july and i wanted to add an else so this is what i came up with!
if month == "august":
    print ("Happy birthday month to you!")
else: print ("Happy non birthday month to you!")
