# assert.py

chars = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon']

def display(elem):
    assert type(elem) is int, 'Argument must be integer.'
    print('List element', elem, '=', chars[elem])

elem = 4
display(elem)

elem = elem / 2
display(elem)


