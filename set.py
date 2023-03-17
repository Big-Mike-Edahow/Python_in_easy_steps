# set.py
# Examples of Python tuples and sets

# Initialize tuple zoo
zoo = ("Kangaroo", "Leopard", "Moose")

print("Tuple: ", zoo, "\tLength: ", len(zoo))
print(type(zoo), "\n")

# Initialize set bag, and then add an element
bag = {"Red", "Green", "Blue"}
bag.add("Yellow")

print("Set: ", bag, "\tLength: ", len(bag))
print(type(bag), "\n")

print("Is Green In bag Set?: ", 'Green' in bag)
print("Is Orange In bag Set?: ", 'Orange' in bag, "\n")

# Initialize a new set box, and return items common to both sets
box = {"Red", "Purple", "Yellow"}
print("Set: ", box, "\t\tLength: ", len(box))
print("Common To Both Sets: ", bag.intersection(box))

