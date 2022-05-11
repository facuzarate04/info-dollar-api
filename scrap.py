import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

class DollarBlueScrap:

    def get_data():

        url = os.getenv('SCRAP_URL')
        page = requests.get(url, timeout=5)
        soup = BeautifulSoup(page.text, 'html.parser')

        table = soup.find("table", attrs={"id":"BluePromedio"})
        title = table.find("td", attrs={"class":"colNombre"}).text
        date = table.find("td", attrs={"class":"colFecha"}).text
        variation = table.find("td", attrs={"class":"colVariacion"}).text
        
        prices = table.find_all("td", attrs={"class":"colCompraVenta"})
        values = []

        for price in prices:
            values.append(price.contents[0])


        data = {
            'title': title,
            'date': date,
            'values' : {
                'buy': values[0],
                'sell': values[1]
            },
            'variation': variation,
        }

        return data

class DollarOficialScrap:

    def get_data():

        url = os.getenv('SCRAP_URL')
        page = requests.get(url, timeout=5)
        soup = BeautifulSoup(page.text, 'html.parser')

        table = soup.find("table", attrs={"id":"Promedio"})
        title = table.find("td", attrs={"class":"colNombre"}).text
        date = table.find("td", attrs={"class":"colFecha"}).text
        prices = table.find_all("td", attrs={"class":"colCompraVenta"})

        values = []
        for price in prices:
            values.append(price.contents[0])

        variation = table.find("td", attrs={"class":"colVariacion"}).text

        data = {
            'title': title,
            'date': date,
            'values' : {
                'buy': values[0],
                'sell': values[1],
                'w_tax': values[2],
                'w_full_tax': values[3]
            },
            'variation': variation
        }

        return data
