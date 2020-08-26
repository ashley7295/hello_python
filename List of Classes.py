
#list
classes = []

#asking for all of the classes separated by a comma
class_name = (input("Please enter the names of all of the classes you are taking, separate with a comma: "))


#prints this message to the user
print ("Here are the classes you are taking: ")

#splits the inital input by the comma (and a space) and puts it into a new list called individual classes
individual_classes = class_name.split(", ")

#for each item in the new list, add it to the classes list
for i in individual_classes:
    classes.append(i)

#prints the whole list
print(classes)

#for each item in the classes list, print a class on a separate line
for one_class in classes:
    print(one_class)

 