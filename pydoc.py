
import requests,pydoc,webbrowser

#sprint(pydoc.__doc__)
  
#print("Using __doc__:")
#print(requests.__doc__)
res=requests.__doc__
print(res)
#print(my_function.__doc__)
f = open('C:/Users/VC/Desktop/PydocWebInterface/sample.html','w')

message = """
<html>
	<head></head>
	<body>
		<input type="text" id="str" placeholder="Search string"/>
		<input type="button" id="search" value="Search"/>
	</body>
</html>
"""

f.write(message)
f.close()
