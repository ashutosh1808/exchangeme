from flask import Flask,render_template,request
from forex_python.converter import CurrencyRates,CurrencyCodes


app=Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/convert")
def convert():
	try:
		amt=float(request.args.get("amt"))
		from_currency=request.args.get("from_currency")
		to_currency=request.args.get("to_currency")
		c=CurrencyRates()
		c1=CurrencyCodes()
		res=c.convert(from_currency,to_currency,amt)
		res=round(res,0)
		msg=str(c1.get_symbol(from_currency))+str(amt)+" = "+str(c1.get_symbol(to_currency))+str(res)
		return render_template("home.html",msg=msg)
	except Exception as e:
		return render_template("home.html",msg=e)


if __name__=="__main__":
	app.run(debug=True,use_reloader=True)