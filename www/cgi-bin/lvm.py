#!/usr/bin/python36

import subprocess as sp
import cgi

print("content-type: text/html")
print()

print('''<form action="http://192.168.43.19/cgi-bin/lvm_file.py">
     Enter ip: <input name='ip'/></br>
     Device:<input name='d'/></br>
     volume group:<input name='v'/></br>
     Logical volume:<input name='l'/></br>
     size_lvm:<input name='s'/></br>
     Mount point:<input name = 'm'/></br>
<input type='submit'/>
  </form>''')            
