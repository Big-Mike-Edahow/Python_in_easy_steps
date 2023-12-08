# polymorph.py

from Duck import *
from Mouse import *

def describe(object):
    object.talk()
    object.coat()

donaldDuck = Duck()
mickeyMouse = Mouse()

describe(donaldDuck)
describe(mickeyMouse)
print()
