import argparse
import collections
import datetime
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader, select_autoescape


def get_path(path):
    parser = argparse.ArgumentParser(description='Программа получает путь к файлу')
    parser.add_argument('-f', '--file', default=path, help='Файл с продукцией')
    args = parser.parse_args()
    new_path = args.data

    return new_path


def count_age():
    open_year = 1920
    current_year = datetime.date.today().year
    age = current_year - open_year
    if age == 1 or age % 100 == 1:
        return str(age) + ' год'
    if age == 2 or age % 100 == 2 or age % 100 == 3 or age % 100 == 4:
        return str(age) + ' года'
    else:
        return str(age) + ' лет'


def get_products(file_path):
    data = pandas.read_excel(file_path,
                             keep_default_na=False).to_dict(orient='records')
    wines = collections.defaultdict(list)
    for wine in data:
        wines[wine['Категория']].append(wine)
    return sorted(wines.items())


def main():
    load_dotenv()
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml']))
    template = env.get_template('template.html')
    path = os.getenv('FILE')
    file_path = get_path(path)
    products = get_products(file_path)
    company_age = count_age()
    rendered_page = template.render(company_age,
                                    products)
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
