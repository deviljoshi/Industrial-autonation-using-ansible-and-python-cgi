#!/usr/bin/python36

import subprocess as sp
import cgi

print("content-type:text/html")
print()

print('''<form action="http://192.168.43.19/cgi-bin/service_actions_stop.py">
  Enter IP: <input name= 'ip'/></br>
  Enter name: <input name='n'/></br>
 <input type='submit'/>
  </form> ''')

