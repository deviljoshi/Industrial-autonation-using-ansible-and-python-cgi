#!/usr/bin/python36

import subprocess as sp
import cgi


print("content-type:text/html")
print()


form=cgi.FieldStorage()
ip=form.getvalue('ip')

print(ip)

cmd=sp.getstatusoutput("sudo ansible-playbook /var/www/cgi-bin/ansible_codes/web1.yml")

if (cmd[0]) ==0:
        print("Deployed webserver successfully</br>")
else:
        print("Not able to configure")

print("<button><a href=http://192.168.43.19/cgi-bin/menu.py>Go Back to Menu</a></button>")


