#!/usr/bin/python36

import subprocess as sp
import cgi

print("content-type: text/html\n")

print("<form action=http://192.168.43.102/cgi-bin/rm_user.py>")
print("Enter user name: <input name='u'/>")
print('''<button onclick="myfunction()"> Submit </button>
<script>
function myfunction(){
alert("User removed Successfully ");
}   
</script>''')
print("</form></br>")


