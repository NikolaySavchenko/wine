from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from utils import get_winery_age, get_beverages_from_file
import argparse


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    parser = argparse.ArgumentParser(description='Input Excel file path')
    parser.add_argument('filepath', help='Input Excel file path')
    file_path = parser.parse_args().filepath
    rendered_page = template.render(beverages=get_beverages_from_file(file_path),
                                    age=get_winery_age())

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

if __name__ == '__main__':
    main()

