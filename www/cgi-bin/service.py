#!/usr/bin/python36

import subprocess as sp
import cgi


print("content-type: text/html")
print()

print('''<form action="http://192.168.43.19/cgi-bin/service_file.py">
 "Enter Service Name:" <input name='s'/></br>
 "Enter Ip: <input name='ip'/></br>
 <input type='submit'/>
</form>
''')

