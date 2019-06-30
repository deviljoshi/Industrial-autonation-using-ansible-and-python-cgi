#!/usr/bin/python36

import subprocess as sp
import os
import cgi

print("content-type: text/html")
print()

print('''<form action="http://192.168.43.19/cgi-bin/web_file.py">
Enter ip:<input name='ip'></br>
<input type='submit'/>
</form>''')

#cmd=sp.getstatusoutput("sudo ansible-playbook /var/www/cgi-bin/ansible_codes/web1.yml")

#if (cmd[0]) ==0:
#	print("Deployed webserver successfully</br>")
#else: 
#	print("Not able to configure")

#print("<button><a href=http://192.168.43.19/cgi-bin/menu.py>Go Back to Menu</a></button>")


