#!/usr/bin/python36

import subprocess

print("content-type: text/html")
print()


x = "sudo docker ps -a"
output = subprocess.getoutput(x)


container_list = output.split("\n")



#print("<iframe width='100%' name='myconsole'></iframe>")



print("""

<html>
<title>W3.CSS Template</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
body,h1,h2,h3,h4,h5,h6 {font-family: "Raleway", sans-serif}

body, html {
  height: 100%;
  line-height: 1.8;
}

/* Full height image header */
body
{
background-image:url("/images/nn5.png");

background-attachment:fixed;
background-size: 100% 100%;
padding:20;
}


.w3-bar .w3-button {
  padding: 16px;
}
</style>

<body>

<h1 align=center class="w3-jumbo w3-text-black">CONTAINERS LIVE STATUS</h1>

<table class="w3-large w3-text-black" border='5' width='100%'>
<tr>
<th>Container Name</th>
<th>Image Name</th>
<th>Status</th>
<th>Start</th>
<th>Stop</th>
<th>Terminate</th>
<th>Console</th>
</tr>

</body>

""")


for c  in container_list[1:]:
	if "Up" in c:
		cstatus = "running"
	elif "Exited" in c:
		cstatus = "stopped"
	else:
		cstatus = "unknown status"
	c_details  =  c.split()
	
#	print(c_details)	
	
	cname =  c_details[-1]
	imagename = c_details[1]

	print('''

	<tr>
	<td>{}</td>
	<td>{}</td>
	<td>{}</td>
	<td><a href='http://192.168.43.252/cgi-bin/docker_start.py?s={}'>Start</a></td>
	<td><a href='http://192.168.43.252/cgi-bin/docker_stop.py?s={}'>Stop</a></td>
	<td><a href='http://192.168.43.252/cgi-bin/docker_terminate.py?s={}'>Terminate</a></td>'''.format(cname, imagename, cstatus, cname, cname, cname ))
	#print(c_details[-2])	
	if(('tcp' in c_details[-2]) == False ):
		print(c_details)


#		print(x[1])
		print("<td><a target='myconsole' >Down</a></td>")
		print("</tr>")

		
	else :
		x=(c_details[-2].split(':'))
	#	print(c_details)			
		y=x[1]
	#	print(y)
		port=y.split('-')[0]
		print("<td><a target='myconsole' href='https://192.168.43.252:{}'>Console</a></td>".format(port))
		print("</tr>")



	

print("</table>")

print('''

</br> <iframe width='100%' hight='600px' name='myconsole'></iframe>

''')
