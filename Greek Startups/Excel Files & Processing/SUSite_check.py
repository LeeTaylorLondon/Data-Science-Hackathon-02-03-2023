# Author: Lee Taylor
import os
import requests
from typing import Tuple
from URL_Functions import *
from bs4 import BeautifulSoup as BS


def check_html_file(file: str='SU_websites.txt') -> None:
    with open(file, 'r', encoding='utf-8-sig') as f:
        websites = f.readlines()
    with open("websites_check.csv", 'w', encoding='utf-8-sig') as f:
        f.write("Website, HTML\n")
        for website in websites:
            try:
                page = requests.get(website.strip(), headers=HEADERS)
                soup = BS(page.content, 'html5lib')
                error_message = soup.find("h2", class_="mb-10")
                if error_message is not None and error_message.text == "O" \
                                    "ops, an error has occurred. " \
                                    "Page not found or this content " \
                                    "is removed or hidden for review!":
                    f.write(f"NO, {website.strip()}\n")
                else:
                    f.write(f"YES, {website.strip()}\n")
            except:
                f.write(f"{website.strip()}, no\n")


def extract_yes_websites(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
    with open(output_file, 'w', encoding='utf-8-sig') as f:
        yes_websites = [line.split(',')[1].strip() for line in lines[1:] if line.startswith("YES,")]
        for website in yes_websites:
            f.write(website + '\n')


def write_soup_to_file(file: str, directory: str) -> None:
    # Open URLs
    with open(file, 'r', encoding='utf-8-sig') as f:
        urls = f.readlines()
    # Create directory to store .html files
    if not os.path.exists(directory):
        os.makedirs(directory)
    # Traverse URLs
    for i, url in enumerate(urls):
        try:
            page = requests.get(url.strip())
            soup = BS(page.content, 'html5lib')
            if (web_name := url.strip().split('/')[-1]) == '':
                web_name = str(i)
            with open(f"soup_objects/{web_name}.html", 'w',
                      encoding='utf-8-sig') as f:
                f.write(str(soup))
        except:
            print(f"Error fetching URL: {url.strip()}")


if __name__ == '__main__':
    # check_html_file("SU_websites.txt")
    # extract_yes_websites("websites_check.csv", "yes_websites.txt")
    write_soup_to_file('yes_websites.txt', 'soup_objects')
