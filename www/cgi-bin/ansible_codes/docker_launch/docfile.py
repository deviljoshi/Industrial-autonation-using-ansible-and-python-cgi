#!/usr/bin/python36

import subprocess as sp
import cgi

print("content-type: text/html")
print()


form=cgi.FieldStorage()
doc_name=form.getvalue('s')
print(doc_name)

form_1=cgi.FieldStorage()
img_name=form_1.getvalue('i')

print(img_name)

f1=open("/var/www/cgi-bin/ansible_codes/keywords.py", mode='w+')
f1.write('doc_name: {}\nimg_name: {}'.format((doc_name),(img_name)))
f1.close()

print(doc_name)
print(img_name)

cmd=sp.getstatusoutput("sudo ansible-playbook  /var/www/cgi-bin/ansible_codes/docker_launch/dockerlaunch.yml")

print(cmd)
if(cmd[0]==0):
	print("docker launched successfully")
else:
	print("Unable to configure")
