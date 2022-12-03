from flask import Flask,render_template
from forex_python.converter import CurrencyRates


app=Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")



if __name__=="__main__":
	app.run(debug=True,use_reloader=True)