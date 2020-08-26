
#asking for user input
user_sentance = (input("please enter a sentance to be turned into camelCase: "))


#taking out the spaces
sentance = user_sentance.split(" ")



#asking if any character int he users sentace is a digit and printing a message if it is
if any(chr.isdigit() for chr in user_sentance):
    print ("please do not include numbers")
else:
    #skipping the first letter, capitalize the letter in camelCase
    print (sentance[0] + "".join(map(str.capitalize, sentance[1:])))




