#!/usr/bin/python36

import subprocess as sp
import cgi

print("content-type: text/html")
print()

form=cgi.FieldStorage()
access_key=form.getvalue('a')

form1=cgi.FieldStorage()
secret_key=form1.getvalue('s')

print(access_key)
print(secret_key)

f1=open("/var/www/cgi-bin/ansible_codes/keywords.py", mode='+w')
f1.write("access_code: {}\nsecret_key: {}".format(access_key,secret_key))
f1.close()

cmd=sp.getoutput("sudo ansible-playbook /var/www/cgi-bin/ansible_codes/ec2/ec2InstanceLaunch.yml")
print(cmd)


if cmd[0]==0:
	print("launched successfully")
else:
	print("unable to configure")



