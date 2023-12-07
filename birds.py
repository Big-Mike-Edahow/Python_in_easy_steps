# birds.py

from Songbird import *

rainbowLorikeet = Songbird("Koko", "Tweet, tweet!")
print(rainbowLorikeet.name, "Id:", id(rainbowLorikeet))
rainbowLorikeet.sing()
del rainbowLorikeet

kingfisher = Songbird("Louie", "Chirp, chirp!")
print(kingfisher.name, "Id:", id(kingfisher))
kingfisher.sing()
del kingfisher

learsMacaw = Songbird("Misty", "Squawk, squawk!")
print(learsMacaw.name, "Id:", id(learsMacaw))
learsMacaw.sing()
del learsMacaw


