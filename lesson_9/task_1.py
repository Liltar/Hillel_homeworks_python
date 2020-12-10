import csv
with open('tz_opendata_z01012020_po01122020.csv', 'r', encoding='utf-8') as f:
    csv_file = csv.DictReader(f)
    for line in csv_file:
        print(line)