from textblob import TextBlob
from flask import Flask, render_template, request
from scraper import scrape

app = Flask(__name__)

@app.route('/', host="ibmappendly.herokuapp.com")
def student():
   return render_template('index.html')

@app.route('/result', methods = ['POST', 'GET'], host="ibmappendly.herokuapp.com")
def result():
   if request.method == 'POST':
      result = request.form['Name']
      result = scrape(result)
      price = result[0]
      rating = result[1]
      value = result[2]
      warranty = result[3]
      return render_template("index.html", price = price, rating = rating, value = value, warranty = warranty)

if __name__ == '__main__':
   app.run(debug=True)