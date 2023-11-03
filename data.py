# data.py

import pickle, os
if not os.path.isfile('pickle.dat'):
    data = [0, 1]

    data[0] = input("\nEnter topic: ")
    data[1] = input("Enter series: ")

    file = open('pickle.dat', 'wb')
    pickle.dump(data, file)
    file.close
    print()
else:
    file = open('pickle.dat', 'rb')
    data = pickle.load(file)
    file.close()

    print("\nWelcome back to:\n", data[0], "\n", data[1], "\n")

