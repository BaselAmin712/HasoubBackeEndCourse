import csv
def main():
    
    with open('12_records_manager_12_3_24/records.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'age'])
        writer.writerow(['John Doe', 30])

    
if __name__ == "__main__":
    main()