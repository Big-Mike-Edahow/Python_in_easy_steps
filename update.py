# update.py

text = "The political slogan \"Workers of the world unite!\"\n is from The Communist Manifesto."

with open('update.txt', 'w') as file:
    file.write(text)
    print("\nWithin the \033[1mwith\033[0m block, is the file closed?", file.closed)

print("\nAfter the \033[1mwith\033[0m block, is the file now closed?", file.closed)

with open('update.txt', 'r+') as file:
    text = file.read()
    print("\nString:", text, "\n")

    print("Current position in the file:", file.tell())
    position = file.seek(33)
    print("New position in the file:", file.tell())

    file.write('all lands')
    file.seek(60)
    file.write('the tombstone of Karl Marx.')

    file.seek(0)
    text = file.read()
    print("\nString:", text, "\n")

