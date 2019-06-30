#!/usr/bin/python36

import subprocess as sp
import cgi


print("content-type: text/html")
print()

print('''<form action=http://192.168.43.19/cgi-bin/ansible_codes/groupadd/groupfile.py>
"Enter group name:" <input name= 'n'></br>
<input type= 'submit'/>
</form>
''')


