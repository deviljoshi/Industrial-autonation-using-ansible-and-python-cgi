#!/usr/bin/python36

import subprocess as sp
import cgi

print("contetn-typr:text/html")
print()

form=cgi.FieldStorage()
ip=form.getvalue('ip')

print(ip)

f1=open("/var/www/cgi-bin/ansible_codes/keywords.py", mode='w+')
f1.write("ip: {}".format(ip))
f1.close()

cmd=sp.getstatusoutput("sudo ansible-playbook /var/www/cgi-bin/ansible_codes
