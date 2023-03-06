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


def extract_text(directory, headers=True):
    # Loop through all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a .html file
        if filename.endswith(".html"):
            file_path = os.path.join(directory, filename)
            with open(file_path, "r", encoding='utf-8-sig') as file:
                soup = BS(file, 'html5lib')

                # Find all HTML elements that contain the main content
                if headers:
                    content_elements = soup.find_all(
                        ["p", "h1", "h2", "h3", "h4", "h5", "h6", "a", "li", "span", "strong", "em"])
                elif not headers:
                    content_elements = soup.find_all(["p", "a", "li", "span", "strong", "em"])

                # Concatenate the text from all content elements
                content = [element.text.strip() for element in content_elements]
                for i, v in enumerate(content):
                    content[i] = v.replace('\n', '')
                    content[i] = content[i].replace('  ', '')

                # Remove keywords
                content = [element for element in content if element.strip() != '']  # Remove blanks
                content = [element for element in content if
                           len(element.split()) > 8]  # Remove lines with less than X words
                # content = [element for element in content if not element.lower().__contains__('site')]
                content = [element for element in content if not element.lower().__contains__('cookie')]
                content = [element for element in content if not element.lower().__contains__('sign in')]
                content = [element for element in content if not element.lower().__contains__('instagram')]
                content = [element for element in content if not element.lower().__contains__('contact us')]

                # Combine content into a string
                content = '\n'.join(set(content))

                # Write the extracted text to a file
                # output_file = os.path.splitext(file_path)[0] + ".txt"
                with open(f'soup_to_text/{filename}.txt', "w", encoding='utf-8-sig') as output:
                    output.write(content)
    # Mark EOF
    pass


if __name__ == '__main__':
    # check_html_file("SU_websites.txt")
    # extract_yes_websites("websites_check.csv", "yes_websites.txt")
    # write_soup_to_file('yes_websites.txt', 'soup_objects')
    extract_text("soup_objects")
