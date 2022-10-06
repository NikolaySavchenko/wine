from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from secondary_functions import winery_age, data_from_file
import argparse


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    parser = argparse.ArgumentParser('Input Excel file address')
    parser.add_argument('filepath')
    file_address = parser.parse_args().filepath
    rendered_page = template.render(wine=data_from_file(file_address), age=winery_age())

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

if __name__ == '__main__':
    main()

