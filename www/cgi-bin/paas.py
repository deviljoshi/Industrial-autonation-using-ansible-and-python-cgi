#!/usr/bin/python36

import subprocess as sp
import cgi

print("content-type: text/html")
print()


print('''<form action="http://192.168.43.252/cgi-bin/paas_file.py">
     Enter UserName :<input name='u'/></br>
     Enter Password :<input name='p' type='password'/></br>
<input type='submit'/>

  </form>''')            
