#!/usr/bin/python36


import subprocess as sp
import cgi

print("content-type:text/html")
print()



form=cgi.FieldStorage()
device=form.getvalue('d')
#print(device)

form1=cgi.FieldStorage()
vg_name=form1.getvalue('v')
#print(vg_name)

form2=cgi.FieldStorage()
lv_name=form2.getvalue('l')
#print(lv_name)

form3=cgi.FieldStorage()
size_lv=form3.getvalue('s')
#print(size_lv)

form4=cgi.FieldStorage()
mount=form4.getvalue('m')
#print(mount)

form5=cgi.FieldStorage()
ip=form5.getvalue('ip')
#print(ip)


f1=open("/var/www/cgi-bin/ansible_codes/keywords.py", mode='w+')
f1.write("ip: {}\ndevice: {}\nvg_name: {}\nlv_name: {}\nsize_lv: {}\nmount: {}".format(ip,device,vg_name,lv_name,size_lv,mount))
f1.close()

cmd=sp.getstatusoutput("sudo ansible-playbook /var/www/cgi-bin/lvm.yml")
#print(cmd)

if (cmd[0]==0):
        print("lvm created successfully")
else:
        print("unable to create")
