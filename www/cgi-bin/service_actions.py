#!/usr/bin/python36


import subprocess as sp
import cgi


print("content-type: text/html")
print()

form= cgi.FieldStorage()
ip=form.getvalue('ip')
print(ip)

form1=cgi.FieldStorage()
name=form1.getvalue('n')
print(name)

f1=open("/var/www/cgi-bin/ansible_codes/keywords.py", mode='w+')
f1.write("ip: {}\nname: {}".format(ip,name))
f1.close()


cmd=sp.getstatusoutput("sudo ansible-playbook /var/www/cgi-bin/service_start.yml")
#print(cmd)

if (cmd[0]==0):
	print("service started successfully")
else:
	print("unable to start")

print("<button><a href=http://192.168.43.19/cgi-bin/menu.py>Go back to Main Menu</a></button>")
