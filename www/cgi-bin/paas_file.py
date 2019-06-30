#!/usr/bin/python36


import subprocess as sp
import cgi
import random

print("content-type:text/html")
print()


form3=cgi.FieldStorage()
name=form3.getvalue('u')
passwd=form3.getvalue('p')
#print(size_lv)

x=random.randint(1111,9999)

cmd = sp.getstatusoutput("sudo docker run -dit -p {}:4200  python".format(x))


print('''
<h1><a href='https://192.168.43.252:{}' target='mycaas' >Click Here for Container as a service </a></h1>

<iframe width = '800px'  height='800px'  name='mycaas'></iframe>'''.format(x))
