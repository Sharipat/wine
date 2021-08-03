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
    parser.add_argument('-d', '--data', default=path, help='Файл с продукцией')
    args = parser.parse_args()
    new_path = args.data

    return new_path


def count_age():
    open_date = 1920
    current_date = datetime.date.today().year
    age = current_date - open_date
    if age == 1 or age % 100 == 1:
        return str(age) + ' год'
    if age == 2 or age % 100 == 2 or age % 100 == 3 or age % 100 == 4:
        return str(age) + ' года'
    else:
        return str(age) + ' лет'


def convert_to_dict(path_file):
    excel_data = pandas.read_excel(
        get_path(path_file), keep_default_na=False).to_dict(orient='records')
    wines = collections.defaultdict(list)
    for wine in excel_data:
        wines[wine['Категория']].append(wine)
    return sorted(wines.items())


def main():
    load_dotenv()
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml']))
    template = env.get_template('template.html')
    path_file = os.getenv('EXCEL_DATA')
    products = convert_to_dict(path_file)
    company_age = count_age()
    rendered_page = template.render(company_age,
                                    products)
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
