import os
import csv

budget_data=os.path.join("budget_data.csv")

total_months = []
total_PL = []
monthly_PL_change = []
 
with open(budget_data, newline='') as csvfile:

    csvreader = csv.reader(csvfile,delimiter=",") 
    header = next(csvreader)  

    for row in csvreader: 
        total_months.append(row[0])
        total_PL.append(int(row[1]))

    for i in range(len(total_PL)-1):
        monthly_PL_change.append(total_PL[i+1]-total_PL[i])
        
max_increase_value = max(monthly_PL_change)
max_decrease_value = min(monthly_PL_change)

max_increase_month = monthly_PL_change.index(max(monthly_PL_change)) + 1
max_decrease_month = monthly_PL_change.index(min(monthly_PL_change)) + 1 

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_PL)}")
print(f"Average Change: {round(sum(monthly_PL_change)/len(monthly_PL_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

write_file = f"pybank_analysis.txt"

filewriter = open(write_file, mode = 'w')

filewriter.write("Financial Analysis\n")
filewriter.write("--------------------------\n")
filewriter.write(f"Total Months: {len(total_months)}\n")
filewriter.write(f"Total: ${sum(total_PL)}\n")
filewriter.write(f"Average Change:{round(sum(monthly_PL_change)/len(monthly_PL_change),2)}\n")
filewriter.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})\n")
filewriter.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})\n")
filewriter.close()