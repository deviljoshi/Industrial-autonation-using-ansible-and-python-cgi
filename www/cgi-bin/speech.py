#!/usr/bin/python36
import subprocess as sp
import cgi
print("content-type: text/html")
print()
mydata=cgi.FieldStorage()
y=mydata.getvalue('q')

if "free ram" in y:
	print("<meta http-equiv='refresh' content=0;url='http://192.168.43.252/cgi-bin/free_ram.py'/>")

elif "docker" in  y:
	print("<meta http-equiv='refresh' content=0;url='http://192.168.43.252/cgi-bin/xxx.py'/>")

elif "logical volume" in y or "lvm" in y:
        print("<meta http-equiv='refresh' content='0;url=http://192.168.43.115/cgi-bin/logicalpart_html.py'/>")

elif "configure" in y and "job" in y:
        print("<meta http-equiv='refresh' content='0;url=http://192.168.43.115/cgi-bin/cron_html.py'/>")

elif "send" and "mail" in y:
        print("<meta http-equiv='refresh' content='0;url=http://192.168.43.115/mail_form.html'/>")

elif "aws instance" in y or "aws" in y:
	print("<meta http-equiv='refresh' content='0;url=http://192.168.43.115/aws_ec2_form.html'/>")

elif "upload a file" in y or "put s3 bucket" in y:
	print("<meta http-equiv='refresh' content='0;url=http://192.168.43.115/s3_put_form.html'/>")

elif "delete a file" in y or "s3 bucket delete" in y:
   	print("<meta http-equiv='refresh' content='0;url=http://192.168.43.115/s3_delobj_form.html'/>")

elif "download a file" in y or "get s3 bucket" in y:
	print("<meta http-equiv='refresh' content='0;url=http://192.168.43.115/s3_get_form.html'/>")

elif "yum configure" in y:
	print("<meta http-equiv='refresh' content='0;url=http://192.168.43.115/yum_form.html'/>")

elif "java" in y:
	print("<meta http-equiv='refresh' content='0;url=http://192.168.43.115/java_form.html'/>")

elif "python" in y:
	print("<meta http-equiv='refresh' content='0;url=http://192.168.43.115/python_form.html'/>")

elif "configure" in y and "IAAS" in y and "web server" in y:
	print("<meta http-equiv='refresh' content='0;url=http://192.168.43.115/iaas_form.html'/>")

elif "IAAS" in y and "client" in y:
	print("<meta http-equiv='refresh' content='0;url=http://192.168.43.115/iaas_client_form.html'/>")
