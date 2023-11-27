# address.py

from Bird import *

chick = Bird('Cheep, cheep!')
chick.age = '1 week'

print("\nChick says:", chick.talk())
print("\nChick age:", chick.age)

chick.age = '2 weeks'
print("Chick now:", chick.age)

setattr(chick, 'age', '3 weeks')

print("\nChick Attributes...")
for attribute in dir(chick):
    if attribute[0] != '_':
        print(attribute, ':', getattr(chick, attribute))

delattr(chick, 'age')
print("\nChick age attribute?", hasattr(chick, 'age'))

