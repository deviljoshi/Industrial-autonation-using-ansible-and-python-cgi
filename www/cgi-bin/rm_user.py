#!/usr/bin/python36
import subprocess as sp
import cgi

print("content-type: text/html")
print()

form=cgi.FieldStorage()
out=form.getvalue("u")

cmd=sp.getoutput("sudo userdel {}".format(out))
print(cmd)

print("<button><a href=http://192.168.43.102/cgi-bin/menu.py>Go to Main Menu</a></button>")

