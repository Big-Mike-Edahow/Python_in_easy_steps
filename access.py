# access.py

file = open('example.txt', 'w')

print("File name:", file.name)
print("File open mode:", file.mode)

print("Readable:", file.readable())
print("Writable:", file.writable())

def get_status(f):
    if (f.closed == True):
        return 'Closed'
    else:
        return 'Open'

print("File status:", get_status(file))
file.close()
print("\nFile status:", get_status(file))

