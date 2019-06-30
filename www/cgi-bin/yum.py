#!/usr/bin/python36

import subprocess as sp
import cgi

print("content-type: text/html")
print()

print('''<form action="http://192.168.43.102/cgi-bin/yum_file.py">
  Enter ip: <input name= 'ip'/>
  <input type ='submit'/>
  </form>
 ''')

