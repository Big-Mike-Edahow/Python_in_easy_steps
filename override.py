# override.py

from Man import *
from Hombre import *

dude = Man('Richard')
guy = Hombre('Ricardo')

dude.speak("It's a beautifl evening.\n")
guy.speak("Es una tarde hermosa.\n")

Person.speak(dude)
Person.speak(guy)

