import pandas

keys = ["nameTranslit",
        "productType",
        "usedProductType",
        "materialCisNumber",
        "materialSource",
        "modelName",
        "supplier",
        "vendorCatalog",
        "sublicense",
        "partnerType",
        "saleLegal",
        "preorder",
        "isMprimeSubscription",
        "isPreorder",
        "brandId",
        "brandName",
        "status",
        "properties",
        "images",
        ]


def converter():
    path = 'data/5_result.json'
    pandas.read_json(path, encoding='windows-1251').to_excel("output/output.xlsx")


def cleaning(src, lst):
    for s in src:
        for i in lst:
            try:
                s.pop(i)
            except Exception:
                continue
        for j in range(5):
            try:
                del s["propertiesPortion"][j]["nameDescription"]
                del s["propertiesPortion"][j]["valueDescription"]
            except KeyError:
                continue
            except IndexError:
                continue


def init_header(src):
    try:
        with open('config.py') as f:
            res = f.readlines()[:38]

        f = open('config.py', 'w+')
        f.seek(0)
        f.close()

        with open('config.py', 'w') as file:
            for r in res:
                file.write(r)
        with open('config.py', 'a') as fl:
            fl.write(src)
    except Exception as ex:
        print(ex)
        return False
    return True

