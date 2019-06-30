#!/usr/bin/python36

import subprocess as sp
import os

print("content-type: text/html")
print()

#print("<body background= './img.jpg'>")

#os.system("tput setaf 1")
print('<body background=./img.jpg >')
print("\t\t\t---------<b>Welcome to my tools</b>---------</br>")
print("<b>Experience remotely setup by just one click</b></br>")
print('''
       Options:</br>
       <a href="http://192.168.43.252/cgi-bin/date.py">1: To check date</a></br>
       <a href="http://192.168.43.252/cgi-bin/cal.py">2: To check cal</a></br>
       <a href="http://192.168.43.252/cgi-bin/file.py">3: To make a file</a></br>
       <a href="http://192.168.43.252/cgi-bin/static_ip/ip_static.py">4: To do static ip</a></br>
       <a href="http://192.168.43.252/cgi-bin/free_ram.py">5: To show free RAM</a></br>
      
       <a href="http://192.168.43.252/cgi-bin/ansible_codes/ec2/ec2_instance.py">6 : To launch ec2 Instance</a></br>
       <a href="http://192.168.43.252/cgi-bin/useradd.py">7 : To add user</a></br>
       <a href="http://192.168.43.252/cgi-bin/ansible_codes/groupadd/groupadd.py">8: To add Group</a></br>
       <a href="http://192.168.43.252/cgi-bin/mail.py">9 : To mail</a></br>
       <a href="http://192.168.43.252/cgi-bin/user_remove.py">10 : To remove user</a></br>
       <a href="http://192.168.43.252/cgi-bin/ansible_codes/docker_launch/dockerlaunch.py">11: To launch docker</a></br>
       <a href="http://192.168.43.252/cgi-bin/web1.py">12: To configure webserver</a></br> 
       <a href="http://192.168.43.252/cgi-bin/yum.py">13: To configure yum in RHEL</a></br>
       <a href="http://192.168.43.252/cgi-bin/docker_caas.py">14: To configure webserver in docker (docker as CAAS service)</a></br>
       <a href="http://192.168.43.252/cgi-bin/lvm.py">15: To make lvm partition</a></br>
       <a href="http://192.168.43.252/cgi-bin/service.py">16: Services</a></br>
       <a href="http://192.168.43.252/cgi-bin/service_Start.py">17: To Start a Service</a></br>
       <a href="http://192.168.43.252/cgi-bin/service_Stop.py">18: To Stop a service</a></br>
       <a href="http://192.168.43.252/cgi-bin/stass1.py">14: To configure Stass as a service</a></br>
       <a href="http://192.168.43.252/cgi-bin/paas.py">14: To configure paas as a service</a></br>
       <a href="http://192.168.43.252/cgi-bin/xxx.py">14: To get Docker status</a></br>
       </body>''')
