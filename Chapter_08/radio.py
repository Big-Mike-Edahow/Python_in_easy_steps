# radio.py

import cgi

data=cgi.FieldStorage()

answer = data.getvalue('category')

if answer == 'Markup':
    result = answer + ' is correct.'
else:
    result = answer + ' is incorrect.'

print('Content-type:text/html\r\n\r\n')
print('<DOCTYPE html>')
print('<html lang="en">')
print('<head>')
print('<meta charset="UTF-8">')
print('<link href="./style.css" type="text/css" rel="stylesheet">')
print('<title>Python Response</title>')
print('</head>')
print('<body>')
print('<main>')
print('<h1>', result, '</h1>')
print('<a href="./radio.html">Back</a>')
print('</main>')
print('</body>')
print('</html>')

