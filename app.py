from flask import Flask, render_template, request
from scraper import scrape
import requests
import json

app = Flask(__name__)

#STORE CONVERSION
data = {}

#INITIAL API CALL AND STORE CONVERSION
def apiInit():
    global data

    #API SETUP
    url = "https://fixer-fixer-currency-v1.p.rapidapi.com/latest"
    headers = {
    "X-RapidAPI-Host": "fixer-fixer-currency-v1.p.rapidapi.com",
    "X-RapidAPI-Key": "e22598e71fmsh79ab05e94e3b5ffp1d6072jsn9b0382f88b54"
    }
    finalURL = url + '?base=INR&symbols=USD%2CJPY%2CEUR'

    #REQUEST
    resp = requests.get(finalURL, headers = headers)
    data = resp.json()

#CONVERSION OF CURRENCIES
def convertCurr(amt):
        #CONVERSION
        amt = float(amt)
        usd = round(amt * data['rates']['USD'], 2)
        jpy = round(amt * data['rates']['JPY'], 2)
        eur = round(amt * data['rates']['EUR'], 2)

        return(usd, jpy, eur)

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
      CPL = int(price)/int(warranty)
      CPL = int(CPL)
      #CURRENCY CONVERSION
      p = convertCurr(price)
      c = convertCurr(CPL)
      return render_template("index.html", price = price, rating = rating, value = value, warranty = warranty, CPL = CPL, pusd = p[0], pyen = p[1], peur = p[2], cusd = c[0], cyen = c[1], ceur = c[2])

if __name__ == '__main__':
    apiInit()
    app.run(debug=True)
