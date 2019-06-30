#!/usr/bin/python36

import subprocess as sp
import cgi

print("content-type:text/html")
print()

form=cgi.FieldStorage()
to=form.getvalue('t')
#print(to)

form1=cgi.FieldStorage()
fr=form1.getvalue('f')
#print(fr)

form2=cgi.FieldStorage()
passwd=form2.getvalue('p')
#print(passwd)

form3=cgi.FieldStorage()
sub=form3.getvalue('s')
#print(sub)

form4=cgi.FieldStorage()
msg=form4.getvalue('m')
#print(msg)


f1=open("/var/www/cgi-bin/ansible_codes/keywords.py", mode='w+')
f1.write("to: {}\nfrom: {}\npassword: {}\nsub: {}\nmsg: {}".format(to,fr,passwd,sub,msg))
f1.close()

cmd=sp.getstatusoutput("sudo ansible-playbook /var/www/cgi-bin/mail.yml")
#print(cmd)

if (cmd[0]==0):
	print("mail sent successfully")
else:
	print("unable to sent")

print("<button><a href=http://192.168.43.19/cgi-bin/menu.py>Go Back to Menu</a></button>")

