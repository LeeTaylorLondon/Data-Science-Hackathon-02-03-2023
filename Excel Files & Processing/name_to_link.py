# Author: Lee Taylor
"""
This code converts a company name from a .csv file into a lowercase string with hyphens
in place of spaces. It first reads in the contents of the file "combined_csv.csv" and
stores the lines in a list. Then it loops through the first line (lines[1:2]), which
should contain the company name, and splits the line into individual words. For each
word, it first checks if the word contains a comma (indicating that it is part of a
company name and address), and if so, it removes the comma and any punctuation from
the word using the remove_punctuation function and converts it to lowercase. If the
word does not contain a comma, it is assumed to be part of the company name and is
processed in the same way. The resulting words are stored in a list called name, and
finally, the elements of the list are joined together with hyphens to form the final
string.
"""
import string


def remove_punctuation(input_string):
    # Create a string of all punctuation characters
    punctuation = string.punctuation
    # Use the `translate` method to remove all punctuation from the input string
    no_punct = input_string.translate(str.maketrans("", "", punctuation))
    # Return the resulting string
    return no_punct


with open("combined_csv.csv", 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()


names = []
for line in lines[1:]:
    name = []
    for item in line.split():
        if item.__contains__(','):
            name.append(remove_punctuation(item.split(',')[0]).lower())
            break
        else:
            name.append(remove_punctuation(item).lower())
    names.append(name)


prefix = 'https://registry.elevategreece.gov.gr/company/'
name_strs = []
for i, v in enumerate(names):
    name_strs.append('-'.join(v))
    name_strs[i] = f"{prefix}{name_strs[i]}/\n"


with open("company_websites.txt", 'w', encoding='utf-8-sig') as f:
    f.writelines(name_strs)
