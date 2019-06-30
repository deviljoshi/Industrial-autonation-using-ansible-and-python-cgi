#!/usr/bin/python36

import subprocess as sp
import cgi

print("content-type: text/html")
print()

print('''<form action="http://192.168.43.19/cgi-bin/mail_file.py">
     To:<input name='t'/></br>
     From:<input name='f'/></br>
     Password:<input name='p' type='password'/></br>
     Subject:<input name='s'/></br>
     Message:<input name = 'm'/></br>
<input type='submit'/>
  </form>''')


     
