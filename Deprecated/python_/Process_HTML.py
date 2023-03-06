# Author: Lee Taylor
from bs4 import BeautifulSoup


def extract_elements(html_text, elm='p'):
    soup = BeautifulSoup(html_text, 'html.parser')
    paragraphs = []
    for p in soup.find_all(elm):
        paragraphs.append(p.text.strip())
    return paragraphs


if __name__ == '__main__':
    # Read .html file
    with open("HTML Files/registry.elevategreece.gov.html",
              'r', encoding='utf-8-sig') as f:
        html_text = f.read()
    # Process .html for P's
    ps = extract_elements(html_text)
    for i,v in enumerate(ps):
        ps[i] = v.strip()
    for p in ps:
        print(p)
