from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
from win10toast import ToastNotifier
#header
header={"User-agent":"Mozilla"}
#apiwebsite
req= Request("https://www.worldometers.info/coronavirus/country/india/" , headers=header)
html = urlopen(req)
obj = bs(html)
#newcases_webscraping
new_cases = obj.find("li", {"class":"news_li"}).strong.text.split()[0]
#deaths_webscraping
death = list(obj.find("li", {"class":"news_li"}).strong.next_siblings)[1].text.split()[0]
#starting notifier
notifier=ToastNotifier()
#printing data
message  = "New Cases - "+ new_cases+"\nDeath - "+death 
#toastnotification
notifier.show_toast(title="COVID-19 Update", msg=message, duration=15, icon_path=r"virus.ico")
