from forex_python.converter import CurrencyRates

c=CurrencyRates()
amt=float(input("enter amt  "))
from_amt=input("convert from? ").upper()
to_amt=input("convert into? ").upper()
res=c.convert(from_amt,to_amt,amt)
print(res)