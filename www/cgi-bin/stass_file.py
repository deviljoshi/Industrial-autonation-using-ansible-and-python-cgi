#!/usr/bin/python36


import subprocess as sp
import cgi

print("content-type:text/html")
print()


form3=cgi.FieldStorage()
size_lv=form3.getvalue('s')
#print(size_lv)



f1=open("/var/www/cgi-bin/ansible_codes/keywords.py", mode='w+')
f1.write("ip: localhost\ndevice: /dev/sdb\nvg_name: xyz\nlv_name: pqr\nsize_lv: {}\nmount: /name".format(size_lv))
f1.close()

cmd=sp.getstatusoutput("sudo ansible-playbook /var/www/cgi-bin/lvm.yml")
#print(cmd)

if (cmd[0]==0):
        print("lvm created successfully")
else:
        print("unable to create")
