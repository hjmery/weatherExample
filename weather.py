import tkinter
import requests
from bs4 import BeautifulSoup
url = "https://www.ksl.com/weather/forecast/Logan"
soup = BeautifulSoup(requests.get(url).content, features='lxml')
#print(soup.prettify())
highs = []
lows = []
for i in soup.find_all('div', attrs = {'class':'highTemp wxnormal'}):
	highs.append(i)
for i in soup.find_all('div', attrs = {'class':'lowTemp'}):
	lows.append(i)

tomorrowHigh = highs[0].text.strip()
tomorrowLow = lows[0].text.strip()

m=tkinter.Tk()

lab1 = tkinter.Label(m, text="high = " + tomorrowHigh, width=25)
lab2 = tkinter.Label(m, text="low = " + tomorrowLow, width=25)
lab1.pack()
lab2.pack()

m.mainloop()