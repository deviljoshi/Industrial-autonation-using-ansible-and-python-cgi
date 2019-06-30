#!/usr/bin/python36
import subprocess as sp
import os
import cgi

print("content-type: text/html")
print()


print(''' <form action=http://192.168.43.252/cgi-bin/ansible_codes/docker_launch/doclaunch.py>
<b>Enter no. of dockers you want to launch:</b><input name='c'/></br>
<b>Enter ip: </b><input name='ip'/></br>
       <a href=http://192.168.43.252/cgi-bin/ansible_codes/docker_launch/doclaunch.py><input type='submit'/></a>
</form>''')

#print("<form action=http://192.168.43.102/cgi-bin/dockerlaunch.yml>")
#print("<form action=http://192.168.43.102/cgi-bin/dockerlaunch.yml>")
#for i in range(c):
#	print("hello")
#print("<form action=http://192.168.43.102/cgi-bin/dockerlaunch.yml>")
