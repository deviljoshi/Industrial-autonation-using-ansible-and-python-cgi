#!/usr/bin/python36

import subprocess as sp
import cgi


print("content-type: text/html")
print()

print('''<form action="http://192.168.43.252/cgi-bin/static_ip/ip_static_file.py">
"Enter connection name:" <input name = 'n'/></br>
"Enter ip address/subnet mask:" <input name ='ip'/></br>
"Enter gateway:" <input name = 'g'/></br>
"Enter DNS:" <input name = 'd'/></br>
<input type='submit'/></br>
</form>
''')

