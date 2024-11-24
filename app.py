import requests

def fetch_page():
    url = "https://www.mercadolivre.com.br/apple-iphone-16-pro-max-1-tb-titnio-branco-distribuidor-autorizado/p/MLB1040287853?pdp_filters=item_id:MLB3845937945#is_advertising=true&searchVariation=MLB1040287853&position=4&search_layout=stack&type=pad&tracking_id=ea7dfe54-81c3-4470-bdf5-988260595219&is_advertising=true&ad_domain=VQCATCORE_LST&ad_position=4&ad_click_id=OTMwMTJkNjMtZjk1Zi00NTAxLTg5Y2EtYzM2MDVlZWI5MjJh"
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    page_content = fetch_page()
    print(page_content)
    