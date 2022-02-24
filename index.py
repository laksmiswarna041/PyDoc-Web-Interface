from flask import Flask,url_for,render_template,request
app = Flask(__name__)

@app.route('/')
def welcome():
   return render_template('home.html')

@app.route('/home')
def home():
   return render_template('home.html')

@app.route('/search',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("search.html",result = result)


if __name__ == '__main__':
   app.run(debug=True)