# PyDoc-Web-Interface
Features:
1. gets the features of any class or module without using the pydoc command
2. also fetches from Python documentation
3. also lists the flags and their usages

Scope:
1. more visual represenation of data
2. structured and more vivid representation
3. Eg pydoc -p 1234 - opens localhost index on server and and there is an unstructured data 

To do:
1. how python actually works
2. how it identifies the arguments
3. how python installation works
4. how python libraries work
5. use API TO RETREIVE DATA 

Some findings:
1. pydoc foo is about equal to python -c "help('foo')

MODULES:
1. Display HTML page to get the data - getData
2. Implement search using regular expresssion - searchString
3. PyDoc implementation(get the body of the text) - pyDoc
4. Show search result - result
5. Display result in a well presented structure - customResult
