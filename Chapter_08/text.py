# text.py

import cgi

data = cgi.FieldStorage()
if data.getvalue('Future Web'):
    text = data.getvalue('Future Web')
else:
    text = "Please Enter Text."

print('Content-type:text/html\r\n\r\n')
print('<!DOCTYPE html>')
print('<html lang="en">')
print('<head>')
print('<meta charset="UTF-8">')
print('<link href="./style.css" type="text/css" rel="stylesheet">')
print('<title>Python Response</title>')
print('</head>')
print('<body>')
print('<main>')
print('<h1>', text, '</h1>')
print('<a href="./text.html">Back</a>')
print('</main>')
print('</body>')
print('</html>')

