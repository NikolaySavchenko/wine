import datetime
import pandas
import collections
from pathlib import Path


def get_winery_age():
    foundation_winery = 1920
    age = datetime.datetime.today().year - foundation_winery
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


def get_from_file(file_path):
    wine_collection = pandas.read_excel(Path(file_path), na_values=['NA'], keep_default_na=False)
    beverages = collections.defaultdict(list)
    for product in wine_collection.to_dict(orient='records'):
        beverages[product['Категория']].append(product)
    return beverages
