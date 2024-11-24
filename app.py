import requests
from bs4 import BeautifulSoup
import time

def fetch_page():
    url = "https://www.mercadolivre.com.br/apple-iphone-16-pro-max-1-tb-titnio-branco-distribuidor-autorizado/p/MLB1040287853?pdp_filters=item_id:MLB3845937945#is_advertising=true&searchVariation=MLB1040287853&position=4&search_layout=stack&type=pad&tracking_id=ea7dfe54-81c3-4470-bdf5-988260595219&is_advertising=true&ad_domain=VQCATCORE_LST&ad_position=4&ad_click_id=OTMwMTJkNjMtZjk1Zi00NTAxLTg5Y2EtYzM2MDVlZWI5MjJh"
    response = requests.get(url)
    return response.text

def parser_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    product_name = soup.find('h1', class_= 'ui-pdp-title').get_text()
    prices : list = soup.find_all('span', class_='andes-money-amount__fraction')
    old_price : int = int(prices[0].get_text().replace('.',''))
    new_price : int = int(prices[1].get_text().replace('.',''))
       
    return {
        'product_name' : product_name,
        'old_price' : old_price,
        'new_price' : new_price
    }
    
    
    
if __name__ == "__main__":
    while True:
        page_content = fetch_page()
        produto_info = parser_page(page_content)
        print (produto_info)
        time.sleep(10)