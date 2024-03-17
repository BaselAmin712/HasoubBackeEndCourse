import csv

def add_record(record_name, amount):
    found_records_list = search(record_name)
    if not found_records_list:
        with open('12_records_manager_12_3_24/records.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([record_name, amount])

def search(record_name):
    pass