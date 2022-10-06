from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from secondary_functions import winery_age, data_from_file
import argparse

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

parser = argparse.ArgumentParser('Input .xlsx file address')
parser.add_argument('file')
file_name = parser.parse_args().file

rendered_page = template.render(wine=data_from_file(file_name), age=winery_age())

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
