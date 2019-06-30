#!/usr/bin/python36

import subprocess as sp


print("content-type: text/html")
print()

cmd=sp.getoutput("sudo cal")
print(cmd)

print("<button><a href=http://192.168.43.19/cgi-bin/menu.py>Go Back to Menu</a></button>")

