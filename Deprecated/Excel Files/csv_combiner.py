# Author: Lee Taylor
import csv
import glob


# List all the CSV files in the current directory
csv_files = glob.glob("*.csv")


# Create a new file to write the combined content
with open("combined_csv_.csv", 'w', encoding='utf-8-sig', newline='') as combined_file:
    writer = csv.writer(combined_file)

    # Write the header row only once
    headers_written = False

    # Loop through each CSV file
    for file in csv_files:
        with open(file, 'r', encoding='utf-8-sig') as csv_file:
            reader = csv.reader(csv_file)

            # Write the header row if it hasn't been written yet
            if not headers_written:
                headers = next(reader)
                writer.writerow(headers)
                headers_written = True

            # Write the rest of the rows
            for row in reader:
                writer.writerow(row)
