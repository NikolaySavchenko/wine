from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from utils import get_winery_age, get_from_file
import argparse


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    parser = argparse.ArgumentParser(description='Input Excel file address')
    parser.add_argument('filepath', help='Input Excel file address')
    file_address = parser.parse_args().filepath
    rendered_page = template.render(wine=get_from_file(file_address), age=get_winery_age())

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

if __name__ == '__main__':
    main()

