import requests
from bs4 import BeautifulSoup



def gather ( currency ):
    url = "https://coinmarketcap.com/currencies/%s/" % currency
    data = requests.get(url )
    soup = BeautifulSoup(data.text , 'html.parser')
    price = soup.find('div' , attrs={"class" : "priceValue___11gHJ"})
    return price.text.replace("$" , "")
print(gather("bitcoin"))


