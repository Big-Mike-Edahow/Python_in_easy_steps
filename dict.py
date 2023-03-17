# dict.py

# Initialize two dictionaries
userSys = {"name" : "Bob", "sys" : "Win"}
userLang = {"name" : "Bob", "lang" : "Python"}

# Merge the two dictionaries together
dict = userSys | userLang

print("Dictionary: ", dict, "\n")
print("Language: ", dict["lang"])
print("Keys: ", dict.keys(), "\n")

# Delete a pair from the dictionary, and add a replacement pair
del dict["name"]
dict["user"] = "Tom"
print("Dictionary: ", dict, "\n")

# Search the dictionary for a specific key
print("Is there a name key?: ", 'name' in dict)

