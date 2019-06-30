#!/usr/bin/python36

import subprocess as sp
import cgi


print("content-type: text/html")
print()


form=cgi.FieldStorage()
name=form.getvalue('n')

f1=open("/var/www/cgi-bin/ansible_codes/keywords.py" , mode='w+')
f1.write("group_name: {}".format(name))
f1.close

cmd=sp.getstatusoutput("sudo ansible-playbook /var/www/cgi-bin/ansible_codes/groupadd/groupadd.yml")

print(cmd)
if(cmd[0]==0):
	print("Groupadd successfully")
else:
	print("unable to configure")
