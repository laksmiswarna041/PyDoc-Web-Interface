# PyDoc-Web-Interface
Features:
1. Module reference from - https://docs.python.org/3/py-modindex
2. also lists the flags and their usages

Scope:
1. more visual represenation of data
2. structured and more vivid representation



Some findings:
1. pydoc foo is about equal to python -c "help('foo')

MODULES:
1. Display HTML page to get the data - getData
2. Implement search using regular expresssion - searchString
3. PyDoc implementation(get the body of the text) - pyDoc
4. Show search result - result
5. Display result in a well presented structure - customResult

Installation & Running procedure:
1. pip install virtualenv
2. mkdir newproj
3. cd newproj
4. virtualenv venv
5. venv\scripts\activate
6. pip install Flask
7. Open CMD and run 'python index.py'
8. The application opens on 127.0.0.1:5000
