import datetime
import pandas
import collections
from pathlib import Path


def get_winery_age():
    age = (datetime.datetime.today().year -
           datetime.datetime(year=1920, month=1, day=1).year)
    if age % 100 == 1:
        return f'{age} год'
    elif 2 <= age % 100 <= 4:
        return f'{age} года'
    elif 5 <= age % 100 <= 20:
        return f'{age} лет'
    elif age % 10 == 1:
        return f'{age} год'
    elif 2 <= age % 10 <= 4:
        return f'{age} года'
    elif 5 <= age % 10 <= 9 or age % 10 == 0:
        return f'{age} лет'


def get_from_file(file_address):
    wine_collection = pandas.read_excel(Path(file_address), na_values=['NA'], keep_default_na=False)
    beverages = collections.defaultdict(list)

    for product in wine_collection.to_dict(orient='records'):
        temp = dict()
        for characteristic in product:
            temp[characteristic] = product[characteristic]
        beverages[product['Категория']].append(temp)

    beverages_sample = dict()
    for category in beverages:
        beverages_sample[category] = list()
        for product in beverages[category]:
            temp = {
                "title": product['Название'],
                "price": int(product['Цена']),
                "image": Path(f"images/{product['Картинка']}"),
                "sort": product['Сорт'],
                "category": product['Категория'],
                "sales": product['Акция']
            }
            beverages_sample[category].append(temp)

    return beverages_sample
