# check.py

import cgi

data=cgi.FieldStorage()

list='<ul>'

if data.getvalue('sailing'):
    list += '<li>' + data.getvalue('sailing')

if data.getvalue('walking'):
    list += '<li>' + data.getvalue('walking')

if data.getvalue('skiing'):
    list += '<li>' + data.getvalue('skiing')

list += '<ul>'

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
print('<h1>', list, '</h1>')
print('<a href="./check.html">Back</a>')
print('</main>')
print('</body>')
print('</html>')

