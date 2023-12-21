import json
from config import *
from headers_cookie import headers, cookies
import requests
from utils import *
import streamlit as st

st.title('Parsing m video')


def test_proxy():
    server = "38.153.31.187:9675"
    proxies = {"http": server, "https": server}

    response = requests.get(
        url=url, proxies=proxies,
        params=params, headers=headers,
        cookies=cookies).json()
    product_ids = response.get('body').get('products')
    st.write(product_ids)


def get_links():
    response = requests.get(url=url, params=params, headers=headers, cookies=cookies).json()
    product_ids = response.get('body').get('products')
    with open('data/1_product_ids.json', 'w') as file:
        json.dump(product_ids, file, indent=4, ensure_ascii=False)

    json_data['productIds'] = product_ids
    response = requests.post(url=url_list, cookies=cookies, headers=headers, json=json_data).json()
    with open('data/2_product_items.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    product_ids_str = ','.join(product_ids)
    params_price['productIds'] = product_ids_str
    response = requests.get(url=url_price, params=params_price, cookies=cookies, headers=headers).json()
    with open('data/3_product_prices.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    item_prices = {}
    material_prices = response.get('body').get('materialPrices')
    for item in material_prices:
        item_id = item.get('price').get('productId')
        base_price = item.get('price').get('basePrice')
        sale_price = item.get('price').get('salePrice')
        bonus_rubles = item.get('bonusRubles').get('total')

        item_prices[item_id] = {
            'base_price': base_price,
            'sale_price': sale_price,
            'bonus_rubles': bonus_rubles
        }
    with open('data/4_item_prices.json', 'w') as file:
        json.dump(item_prices, file, indent=4, ensure_ascii=False)


def get_result():
    with open('data/2_product_items.json') as file:
        product_items = json.load(file)

    with open('data/4_item_prices.json') as file:
        product_prices = json.load(file)

    products_data = product_items.get('body').get('products')
    for item in products_data:
        product_id = item.get('productId')
        if product_id in product_prices:
            prices = product_prices[product_id]

        item['base_price'] = prices.get('base_price')
        item['sale_price'] = prices.get('sale_price')
        item['bonus_rubles'] = prices.get('bonus_rubles')
        item['item_link'] = f'https://www.mvideo.ru/products/{item.get("nameTranslit")}-{product_id}'
        cleaning(products_data, keys)
    with open('data/5_result.json', 'w') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)


st.button('Сбор ссылок', on_click=test_proxy)
# st.write(headers)
# st.button('Получить результат', on_click=get_result)
# st.button('Конвертировать в excel', on_click=converter)
