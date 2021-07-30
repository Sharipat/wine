from http.server import HTTPServer, SimpleHTTPRequestHandler
import datetime
from dateutil.relativedelta import relativedelta
from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas
import collections

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml']))

template = env.get_template('template.html')


def wine_age():
    open_date = 1920
    current_date = datetime.date.today().year
    age = current_date - open_date
    if age == 1 or age % 100 == 1:
        return str(age) + ' год'
    if age == 2 or age % 100 == 2 or age % 100 == 3 or age % 100 == 4:
        return str(age) + ' года'
    else:
        return str(age) + ' лет'


def wine_list(path):
    excel_data_df = pandas.read_excel(
        path, keep_default_na=False).to_dict(orient='records')
    wines = collections.defaultdict(list)
    for wine in excel_data_df:
        wines[wine['Категория']].append(wine)
    return sorted(wines.items())


wine_dict = wine_list('wine.xlsx')

current_age = wine_age()
rendered_page = template.render(wine_age=current_age,
                                wine_dict=wine_dict)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
