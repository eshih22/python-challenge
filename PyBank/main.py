import os
import csv

budget_csv = os.path.join('Resources', 'budget_data.csv')

#initialize the variables
date = []
profit_list = []
column_total = 0

total_change = 0
count = 0

#open the csv file, initialize it to csvreader, and delimit by ","
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip the header row
    next(csvreader, None)           
    
    #initialize the previous_value because there is no "previous" value yet starting off
    previous_value = None
    
    #loop through each row (minus the header)
    for row in csvreader:
        date.append(row[0])
        column_total += int(row[1])
        
        #assigning the current month's P/L to current_value
        current_value = float(row[1])

        if previous_value is not None:
            monthly_change = current_value - previous_value
            #keep a running total of all monthly changes
            profit_list.append(int(monthly_change))
            total_change += monthly_change
            count += 1

        previous_value = current_value

average_change = total_change / count

max_profit = max(profit_list)
min_profit = min(profit_list)

max_index = profit_list.index(max_profit)
min_index = profit_list.index(min_profit)

max_date = (date[max_index + 1])
min_date = (date[min_index + 1])

print("Financial Analysis")
print("---------------------------------")
print(f"Total Months: {len(date)}")
print(f"Total: ${column_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_date} (${max(profit_list)})")
print(f"Greatest Decrease in Profits: {min_date} (${min(profit_list)})")


with open ("main.txt", "w") as file:
    file.write("Financial Analysis" + "\n")
    file.write("---------------------------------" + "\n")
    file.write(f"Total Months: {len(date)} \n")
    file.write(f"Total: ${column_total} \n")
    file.write(f"Average Change: ${average_change:.2f} \n")
    file.write(f"Greatest Increase in Profits: {max_date} (${max(profit_list)}) \n")
    file.write(f"Greatest Decrease in Profits: {min_date} (${min(profit_list)})")

print ("Results have also been exported to main.txt")
