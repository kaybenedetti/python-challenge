import csv
import os
import operator

change = 0
months_list = []
previous = 0
revenue = []
increase = ["", 0]
decrease = ["", 9999999999999]
total_rev = 0
total_changes = 0
biggest_change = 0
unique_months = 0
rev_avg = 0


#remove duplicate function
def remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 

def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total = total + number
    return total / length

#open csv file
csvpath = os.path.join("budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    for row in csvreader:
        #seperate month from day
        month_check = row[0].split('-')
        months_list.append(month_check[1])
        unique_months = remove(months_list)
        #print(len(unique_months))

        #total rev
        total_rev = total_rev + int(row[1])
        # print(total_rev)

        # avg change in revenue 
        change = int(row[1]) - previous
        total_changes = total_changes + change
        avg_total_change = (total_changes / 86)
        # print(avg_total_change)

        if change > biggest_change:
            biggest_change = change

        if (change > increase[1]):
            increase[1] = change
            increase[0] = row[0]
    

        if (change < decrease[1]):
            decrease[1] = change
            decrease[0] = row[0]

            revenue.append(int(row[1]))

    um = len(unique_months)
    print(f"Total Months = {um}")
    print(f"Total Revenue = {total_rev}")
    print(f"Average Total Change = {avg_total_change}")
    print(f"Greatest Increase = {increase}")
    print(f"Greatest Decrease = {decrease}")
    
           
