#!/usr/bin/python36

import subprocess as sp
import cgi

print("contetn-typr:text/html")
print()

form=cgi.FieldStorage()
ip=form.getvalue('ip')

#print(ip)

f1=open("/var/www/cgi-bin/ansible_codes/keywords.py", mode='w+')
f1.write("ip: {}".format(ip))
f1.close()

f2=open("/var/www/cgi-bin/hosts", mode='w+')
f2.write("{}  ansible_user=root  ansible_password=linux".format(ip)) 
f2.close()

cmd=sp.getstatusoutput("sudo ansible-playbook /var/www/cgi-bin/free_ram.yml")

#print(cmd)


print("<button><a href=http://192.168.43.252/cgi-bin/menu.py>Go back to Menu</a></button>")

cmd1=sp.getoutput("sudo curl http://192.168.43.252")
print(cmd1)

#print("<button><a href='http://192.168.43.252/cgi-bin/menu.py'>Go Back to Menu</a></button>")


#print("<button><a href=http://192.168.43.252/cgi-bin/menu.py>Go back to Menu</a></button>")

