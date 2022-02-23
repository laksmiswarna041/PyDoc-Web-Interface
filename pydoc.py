import requests,pydoc,webbrowser,sys,re
#sprint(pydoc.__doc__)
  
#print("Using __doc__:")
#print(requests.__doc__)

search="requests"
match = re.search(r'requests', search)
#search=str(search)
res=requests.__doc__
#print(res)
#print(my_function.__doc__)
f = open('C:/Users/VC/Desktop/PydocWebInterface/sample.html','w')

message = """
<html>
	<head></head>
	<body>
		<input type="text" id="str" placeholder="Search string"/>
		<input type="button" id="search" value="Search" onclick="msg()"/>
	</body>
	<script>
	function msg(){
		let search=document.getElementById("str").value;
		console.log(search)
		console.log({{res}})
	}
	</script>
</html>
"""

f.write(message)
f.close()

