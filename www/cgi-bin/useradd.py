#!/usr/bin/python36

import subprocess as sp
import cgi

print("content-type: text/html\n")

print("<form action=http://192.168.43.19/cgi-bin/user.py>")
print("Enter user name: <input name='u'/>")
print('''<button onclick="myfunction()"> Submit </button>
<script>
function myfunction(){
alert("Useradded Successfully ");
}   
</script>''')
print("</form></br>")





#x=sp.getoutput("id")
#print(x)
#print("useradd successfully")

