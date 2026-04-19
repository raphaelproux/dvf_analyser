'''
Created Date: 2021-12-19 17:47:52
Author: Raphaël Proux
-----
Last Modified: 2021-12-19 19:22:17
Modified By: Raphaël Proux (<raphael.proux@eu.umicore.com>)
-----
Copyright (c) 2021
'''
import re
import numpy as np
from decimal import Decimal, InvalidOperation

import requests
from bs4 import BeautifulSoup

list_sites = {
    'guenno': {
        'url': 'https://www.guenno.com/biens/recherche?realty_type%5B%5D=2&mandate_type=1&min_surface=&town=acigne&price_max=',
    }
}

houses = []

for site_name, site_info in list_sites.items():
    print(f'Site: {site_name}')
    r = requests.get(site_info['url'])
    soup = BeautifulSoup(r.text, "lxml")

    house_list = soup.find(id="listRealtys").find_all("article")

    for house in house_list:
        title = house.find(attrs={'class': "article-title"}).text
        details = f"{house.find(attrs={'class': 'detail'}).text} {house.find(attrs={'class': 'more-about-realty'}).text}"
        details = re.sub(r'\n\s*| +', ' ', details)
        price = house.find(attrs={'class': "realty_price"}).text
        price = re.sub(r' *|€', '', price)
        price = re.sub(r',', '.', price)
        try:
            price = Decimal(price)
        except InvalidOperation:
            price = np.nan
        houses.append({
            "title": title,
            "details": details,
            "price": price
        })

        print(title, details, price)
        
        

        
