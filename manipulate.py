# manipulate.py

def display(s):
    '''Display an argument value.'''
    print(s)

print("\nThe docstring of this function is:")
display(display.__doc__ + "\n")

display(__name__)
display(r'C:\Program Files')

display('\nHello' + ' Python')
display('Python in easy steps\n' [7:])

display('P' in 'Python')
display('p' in 'Python')

print()
__name__ = '__main__'

