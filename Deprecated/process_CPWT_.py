# Author: Lee Taylor
# Objective convert text file to excel file
import PyPDF2


def read_tf(fn="CopyPasteWebsiteText/8.txt"):
    # Open text file
    with open(fn, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()


def extract_text_from_pdf(filename):
    with open(filename, 'rb') as file:
        # pdf = PyPDF2.PdfFileReader(file)
        pdf = PyPDF2.PdfReader(file)
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
        return text


if __name__ == '__main__':
    # lines = read_tf()
    # print(lines)

    pdftext = extract_text_from_pdf('PDFs/Startup Database - Elevate Greece.pdf')
    print(pdftext)
