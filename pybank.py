import os
import csv

budget_data=os.path.join("budget_data.csv")

total_months = []
total_profit = []
monthly_profit_change = []
 
with open(budget_data, newline='') as csvfile:

    csvreader = csv.reader(csvfile,delimiter=",") 
    header = next(csvreader)  

    for row in csvreader: 
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    for i in range(len(total_profit)-1):
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
        
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

write_file = f"pybank_analysis.txt"

filewriter = open(write_file, mode = 'w')

filewriter.write("Financial Analysis\n")
filewriter.write("--------------------------\n")
filewriter.write(f"Total Months: {len(total_months)}\n")
filewriter.write(f"Total: ${sum(total_profit)}\n")
filewriter.write(f"Average Change:{round(sum(monthly_profit_change)/len(monthly_profit_change),2)}\n")
filewriter.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})\n")
filewriter.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})\n")
filewriter.close()