#!/usr/bin/python36


import subprocess as sp
import cgi



print("content-type: text/html")
print()

print("<form action=http://192.168.43.19/cgi-bin/ffile.py></br>")
print("<b>Path with name of file:</b> <input name = 's'/></br>")
#print("<input type='submit'/></br>")
#print("</form></br>")
print('''<button onclick="myfunction()"> Submit </button>
<script>
function myfunction(){
alert("File Created Successfully ");
}
</script>''')
print("</form></br>") 

#print("location: http://192.168.43.19/cgi-bin/file.py")
#print("file created successfully")

