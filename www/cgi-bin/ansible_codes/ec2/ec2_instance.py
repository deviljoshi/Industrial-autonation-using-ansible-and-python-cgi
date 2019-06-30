#!/usr/bin/python36

import subprocess as sp
import cgi


print("content-type: text/html")
print()

print('''<form action="http://192.168.43.19/cgi-bin/ansible_codes/ec2/ec2_details.py">
"Enter Access code: <input name= 'a'/></br>
"Enter Secret key: <input name = 's'/> </br>
<input type='submit'>
</form>
''')
