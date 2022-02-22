import requests,json
response=requests.get('https://docs.python.org/3.8/library/pydoc')
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())
