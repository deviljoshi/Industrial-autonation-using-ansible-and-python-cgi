#!/usr/bin/python36

import subprocess as sp
import cgi

print("content-type: text/html")
print()

form=cgi.FieldStorage()
out=form.getvalue("s")


cmd=sp.getoutput("sudo touch {}".format(out))
print(cmd)

"""print('''<button onclick="myfunction()"> Submit </button>
<script>
function myfunction(){
alert("File Created Successfully! ");
}   
</script>''')
"""
#print("file created successfully</br>")
print("<button><a href=http://192.168.43.19/cgi-bin/menu.py>Go Back to Menu</a></button>")

