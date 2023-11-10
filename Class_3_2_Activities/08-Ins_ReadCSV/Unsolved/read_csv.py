import csv
import os

#csv_path = "Class_3_2_Activities/08-Ins_ReadCSV/Resources/contacts.csv" #look into join function
csv_path = os.path.join("Class_3_2_Activities", "08-Ins_ReadCSV", "Resources", "contacts.csv")
with open(csv_path, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    csv_header = next(csv_reader)
    print(f"CSV Header:  {csv_header}")
    
    for row in csv_reader:
        print(row[0])