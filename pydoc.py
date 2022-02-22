import requests,json
response=requests.get('https://docs.python.org/3.8/library/pydoc')#can get any input


jprint(response.content)
