#!/usr/bin/python36

import subprocess as sp
import cgi

print("content-type:text/html")
print()



form=cgi.FieldStorage()
ip=form.getvalue('ip')
print(ip)

form1=cgi.FieldStorage()
service=form1.getvalue('s')
print(service)


f1=open("/var/www/cgi-bin/ansible_codes/keywords.py", mode='w+')
f1.write("ip: {}\nname: {}".format(ip,service))
f1.close()

cmd=sp.getstatusoutput("sudo ansible-playbook /var/www/cgi-bin/service.yml")
print(cmd)

if (cmd[0]==0):
	print("service installed successfully")
else:
	print("unable to install")


#print('<button><a href="http://192.168.43.19/cgi-bin/stop.py">Stop SErvice</a></button>')

