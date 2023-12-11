# upload.py

import cgi, os

data=cgi.FieldStorage()
upload = data ['filename']
filename = os.path.basename(upload.filename)

with open(filename, 'wb') as copy:
    copy.write(upload.file.read())

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
print('<h1>File uploaded: ', filename, '</h1>')
print('<a href="./upload.html">Back</a>')
print('</main>')
print('</body>')
print('</html>')

