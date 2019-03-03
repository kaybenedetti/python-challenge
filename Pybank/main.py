import csv
import os

average = 0
change = 0
months_list = []
total = 0

#remove duplicate function
def remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 

#open csv file
with open('PyBank/budget_data.csv') as csvfile:

    csvreader = csv.reader(csvfile)
    csv_header = next(csvfile)
    print(f"Columns = {csv_header}")

    for x in csvfile:
        month_check = x[0].split('-')
        months_list.append(month_check)
        unique_months = remove(months_list)
        print(month_check)

