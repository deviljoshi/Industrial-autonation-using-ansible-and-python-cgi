#!/usr/bin/python36

import subprocess as sp
import cgi

print("content-type:text/html")
print()


form=cgi.FieldStorage()
ip=form.getvalue('ip')

f2=open("/var/www/cgi-bin/ansible_codes/keywords.py", mode='w+')
f2.write("ip: {}".format(ip))
f2.close()

#f1=open("/var/www/cgi-bin/hosts", mode='a')
#f1.write("{} ansible_user=root ansible_password=linux".format(ip))
#f1.close()


cmd=sp.getstatusoutput("sudo ansible-playbook /var/www/cgi-bin/yum.yml")
print (cmd)
