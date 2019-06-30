#!/usr/bin/python36

import subprocess as sp
import cgi

print("content-type: text/html")
print()

print('''<form action="http://192.168.43.252/cgi-bin/ram_ip.py">
         "Enter IP address:" <input name='ip'/></br>
         <input type='submit'/>
         </form>''')
