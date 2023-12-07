# inherit.py

from Rectangle import *
from Triangle import *

rect = Rectangle()
trey = Triangle()

rect.set_values(4, 5)
trey.set_values(4, 5)

print("Rectangle area:", rect.area())
print("Triangle area:", trey.area())

