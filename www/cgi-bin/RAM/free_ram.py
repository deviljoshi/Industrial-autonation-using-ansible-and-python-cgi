#!/usr/bin/python36

import subprocess as sp
import cgi

print("content-type: text/html")
print()

print('''<form action="http://192.168.43.102/cgi-bin/RAM/ram_ip.py">
         "Enter IP address:" <input name='ip'/>
         </form>''')
