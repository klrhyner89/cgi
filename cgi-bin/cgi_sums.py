#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()
form = cgi.FieldStorage()
listval = form.getlist('operand')
numbify = [int(x) for x in listval]
print("Content-type: text/plain")
print()
print(sum(numbify))
