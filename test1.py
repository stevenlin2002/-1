import requests
from bs4 import BeautifulSoup
import time

stock = ["5347","2401","2417","2615","6282"]

for i in range(len(stock)):
  stockid = stock[i]
  #if stockid == "5347":
    #url = "https://tw.stock.yahoo.com/quote/"+stockid+".TWO"
  #else:
  #上櫃跟上市差距
  url = "https://tw.stock.yahoo.com/quote/"+stockid+".TW"
  r = requests.get(url)
  soup = BeautifulSoup(r.text,"html.parser")
  price = soup.find("span",class_=["Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)","Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)","Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)"])
  if price== None:
    url = "https://tw.stock.yahoo.com/quote/"+stockid+".TWO"
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    price = soup.find("span",class_=["Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)","Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)","Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)"])
  price=price.getText()
  message = "股票" + stockid + "的即時價格為" + price
  token = "6426346366:AAE7oT_Ds9a_vS2BFT-iGUSudKHNvPOD3qc"
  chat_id = "6148921819"
  url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
  requests.get(url)
    # 每次都停 3 秒
  time.sleep(3)
