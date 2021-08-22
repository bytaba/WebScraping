from re import X
import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook


def gather ( currency ):
    url = "https://coinmarketcap.com/currencies/%s/" % currency
    data = requests.get(url )
    soup = BeautifulSoup(data.text , 'html.parser')
    price = soup.find('div' , attrs={"class" : "priceValue___11gHJ"})
    return price.text.replace("$" , "")

def entry ( price , row ):
    book = load_workbook("../../Ali.xlsx")
    sheet = book.active
    sheet.cell(row ,6).value = price
    book.save("../../Ali.xlsx")

book = load_workbook("../../Ali.xlsx")
sheet = book.active
i = 3

while True :
    name = sheet.cell( i , 2).value
    if name == None:
        break
    print(name)
    entry(gather(name) , i)
    i = i + 1






