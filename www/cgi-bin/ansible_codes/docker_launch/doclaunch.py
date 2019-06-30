#!/usr/bin/python36

import subprocess as sp
import cgi
import os


print("content-type: text/html")
print()

cnt=cgi.FieldStorage()
count=cnt.getvalue('c')
ip=cnt.getvalue('ip')
print(count)
 

f1=open("/var/www/cgi-bin/hosts", mode='w+')
f1.write("{}  ansible_user=root ansible_password=d".format(ip))
f1.close()







print("<form action='http://192.168.43.252/cgi-bin/ansible_codes/docker_launch/docfile.py'>")
for i in range (int(count)):
	print('''
         Enter the name of docker: <input name='s'/></br>
         Enter the image name: <input name= 'i'/></br>''')
print('''
<input type='submit'/>
</form>''')
         
         
	
