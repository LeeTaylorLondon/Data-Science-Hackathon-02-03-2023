# Author: Lee Taylor
# Objective convert text file to excel file
import csv


sta_phrase = 'Startup	Industry	Technology	Region	Employee count	Total funding €	Website'
end_phrase = 'of 711 entries'


def read_tf(fn="Copy Paste Website Text/8.txt"):
    # Open text file
    with open(fn, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines


def index_str(arr, str_):
    """ Return the index of a string in an array. """
    for index, item in enumerate(arr):
        # item = item.strip()
        if item.strip().__contains__(str_):
            return index
    return -1


def write_to_csv(file_path, data):
    data = [[item.strip() for item in line] for line in data]
    with open(file_path, 'w', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        try:
            writer.writerows(data)
        except Exception as e:
            writer.writerow(['Failed', 'Failed', 'Failed', 'Failed', 'Failed'])


def remove_blank_lines(file_path):
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
    lines = [line for line in lines if line.strip()]
    with open(file_path, 'w', encoding='utf-8-sig') as f:
        f.writelines(lines)


if __name__ == '__main__':
    # Define which list of companies to process
    page_number = 1

    for page_number in range(1, 9):
        # Grab lines from text file
        lines = read_tf(f"Copy Paste Website Text/{page_number}.txt")
        # print(lines) # Debug

        # Calculate header and footer indexes
        sta_i = index_str(lines, sta_phrase)
        end_i = index_str(lines, end_phrase)
        print(sta_i, end_i)

        # Extract Useful text into an array of arrays representing lines
        csv_storage, temp_storage = [['Startup','Industry','Technology','Region',
                                     'Employee count','Total funding €','Website']], []
        # lines[x:y] only looks at table text
        for line in lines[sta_i + 1: end_i - 1]:
            line = line.strip()
            # End of line requires special behaviour
            if line.__contains__('Launch icon'):
                line = line.split()
                # Grab E-count & Total Funding €
                for item in line[:2]:
                    temp_storage.append(item)
                csv_storage.append(temp_storage)
                temp_storage = []
            else:
                temp_storage.append(line)

        # print(csv_storage)  # Debug

        # Write to csv
        write_to_csv(f'Excel Files/R{page_number}.csv', csv_storage)
        remove_blank_lines(f'Excel Files/R{page_number}.csv')

    # Mark the end of if-name-main section
    pass