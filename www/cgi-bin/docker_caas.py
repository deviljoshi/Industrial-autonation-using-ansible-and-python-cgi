#!/usr/bin/python36

import subprocess as sp
import cgi
import random

print("content-type: text/html")
print()

x=random.randint(1111,9999)   

cmd = sp.getstatusoutput("sudo docker run -dit -p {}:4200  shellinabox".format(x)) 
print(cmd)
print(x)

#print(cmd)



print('''
<h1><a href='https://192.168.43.19:{}' target='mycaas' >Click Here for Container as a service </a></h1>

<iframe width = '300px'  height='300px'  name='mycaas'></iframe>'''
.format(x))


#sp.getoutput(docker run  -dit -p 1233:4200   /tmp/.X11-unix/:/tmp/.X11-unix  firefox

