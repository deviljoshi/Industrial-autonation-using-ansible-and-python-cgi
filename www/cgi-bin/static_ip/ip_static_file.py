#!/usr/bin/python36

import subprocess as sp
import cgi


print("content-type: text/html")
print()

form=cgi.FieldStorage()
ip_static=form.getvalue('ip')

print(ip_static)

gate=cgi.FieldStorage()
gateway =gate.getvalue('g')
print(gateway)

form3=cgi.FieldStorage()
dns=form3.getvalue('d')
print(dns)

form4=cgi.FieldStorage()
name=form4.getvalue('n')
print(name)

cmd=sp.getoutput("sudo nmcli connection add con-name {} ifname enp0s3 type ethernet ip4 {} gw4 {}".format(name,ip_static,gateway))
cmd1=sp.getoutput("sudo nmcli connection modify {} ipv4.dns {}".format(name, dns))
cmd2=sp.getoutput("sudo nmcli connection up {}".format(name))
cmd3= sp.getoutput("sudo nmcli connection modify {} autoconnect yes".format(name))
cmd4=sp.getoutput("sudo nmcli connection modify enp0s3 autoconnect no")

print(cmd)



