import datetime
import pandas
import collections
from pathlib import Path


def get_winery_age():
    age = datetime.datetime.today().year - 1920
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
        beverages[product['Категория']].append(product)
    return beverages
