# Python Sets

bold = "\033[1m"
from colorama import init, Fore
init (autoreset=True)

# I.
print (bold + "Exercise 1")
print ("")
values = {1, 2, 3, 4, 5}
print ("List (values) : ")
print (values)
values.add(6)
print ("values with (6) :")
print (values)
print ("")

#II.
print (bold + "Exercise 2")
print ("")
fruits = { 'Mango', 'Banana', 'Apple', 'Orange' }
fruits.remove('Banana')
fruits.add('Grapes')
print (fruits)
print ("")

#III.
print (bold + "Exercise 3")
print ("")
set_one = {1, 2, 3, 4}
set_two = {3, 4, 5, 6}
print (set_one)
print (set_two)
print ("")
set_three = set_one.union(set_two)
print ("Union :")
print (set_three)
print ("")
print ("Intersection :")
set_one = {1, 2, 3, 4}
set_two = {3, 4, 5, 6}
set_three = set_two.intersection(set_one)
print (set_three)
print ("'")

#IV.
print (bold + "Exercise 4")
print ("")
colors_one = { 'Red', 'Green', 'Blue'}
colors_two = { 'Yellow', 'Green', 'Orange'}
print (colors_one)
print (colors_two)
print ("")
colors_three = colors_one.difference(colors_two)
print ("Difference :")
print (colors_three)
print ("")
colors_three = colors_two.symmetric_difference(colors_one)
print ("Symmetric Difference :")
print (colors_three)
print ("")

#V.
print (bold + "Exercise 5")
print ("")
cute_animals = { 'Cat', 'Dog', 'Bunny', 'Panda', 'Fish'}
animals = input("Enter an animal! :")
if animals in cute_animals:
	print (animals, "is in the set.")
else:
	print (animals, "is not in the set.")
print ("")
print ("Animals in the set :")
print (cute_animals)
# End