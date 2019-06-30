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

f2=open("/var/www/cgi-bin/hosts", mode='w+')
f2.write("{}  ansible_user=root  ansible_password=linux".format(ip)) 
f2.close()

cmd=sp.getstatusoutput("sudo ansible-playbook ansible_codes/RAM/free_ram.yml")

print(cmd)
