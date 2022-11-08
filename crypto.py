import tkinter as tk
from datetime import datetime
import requests
#tk = Tk()
#tk.mainloop()



url = "https://min-api.cryptocompare.com/data/price?fsym={}&tsyms=USD,EUR"

def get_price(coin, currency):
    try:
        response = requests.get(url.format(coin, currency)).json()
        return response
    except:
        return False

def printcurrencyBTC():
      date_time = datetime.now()
      date_time = date_time.strftime("%H:%M:%S")
      currentPriceB = get_price("BTC", "EUR")
      if currentPriceB:
          return date_time, "BTC", currentPriceB

def printcurrencyETH():
      date_time = datetime.now()
      date_time = date_time.strftime("%H:%M:%S")
      currentPriceE = get_price("ETH", "EUR")
      if currentPriceE:
          return date_time, "ETH", currentPriceE

def affichageBTC():
    global priceBTC
    frameBTC = tk.Frame(top, width=100, height=100, relief='solid', bd=1)
    frameBTC.place(x=10, y=10)
    priceBTC = tk.Label(frameBTC, text='tactic')
    priceBTC.pack()

def affichageETH():
    global priceETH
    frameETH = tk.Frame(top, width=100, height=100, relief='solid', bd=1)
    frameETH.place(x=10, y=50)
    priceETH = tk.Label(frameETH, text='tactac')
    priceETH.pack()


def refreshBTC():
    global priceBTC
    priceBTC.configure(text=printcurrencyBTC())
    top.after(1000, refreshBTC)

def refreshETH():
    global priceETH
    priceETH.configure(text=printcurrencyETH())
    top.after(1000, refreshETH)



top = tk.Tk()
top.geometry("800x800")
top.title("Crypto Monitoring")
affichageBTC(), affichageETH()
refreshBTC(), refreshETH()
top.mainloop()
