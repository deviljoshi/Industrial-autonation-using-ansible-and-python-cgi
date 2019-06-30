#!/usr/bin/python36

import subprocess as sp
import cgi

print("content-type: text/html")
print()

print('''<form action="http://192.168.43.252/cgi-bin/stass_file.py">
     Enter Size in MB :<input name='s'/></br>
<input type='submit'/>
  </form>''')            
