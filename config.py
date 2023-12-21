params = {
    'categoryId': '98',
    'offset': '0',
    'limit': '72',
    'filterParams': [
        'WyJjYXRlZ29yeSIsIiIsIm1pa3NlcnktNDg1Il0=',
        'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
    ],
    'doTranslit': 'true',
}

json_data = {
    'productIds': [],
    'mediaTypes': [
        'images',
    ],
    'category': True,
    'status': True,
    'brand': True,
    'propertyTypes': [
        'KEY',
    ],
    'propertiesConfig': {
        'propertiesPortionSize': 5,
    },
    'multioffer': False,
}

params_price = {
    'productIds': '',
    'addBonusRubles': 'true',
    'isPromoApplied': 'true',
}

url = 'https://www.mvideo.ru/bff/products/listing'
url_list = 'https://www.mvideo.ru/bff/product-details/list'
url_price = 'https://www.mvideo.ru/bff/products/prices'
