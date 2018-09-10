import os
import csv

pybank_analysis="budget_analysis.txt"
budget_data=os.path.join("budget_data.csv")

greatestIncAmt = ["",0]
greatestDecAmt = ["",999999999999999999]

with open(budget_data, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        csv_header=next(csvfile)

        for counter, row in enumerate(csvreader):
            if counter>0:
                break
            firstvalue=row[1]
            firstPL=row[1]

        totalmonths = 2
        total = 0

        for row in csvreader:
            totalmonths = totalmonths +1
            total = total + int(row[1])

            increase = int(row[1]) - int(firstPL)
            firstPL=row[1]

            if(increase > greatestIncAmt[1]):
                greatestIncAmt[0] = row[0]
                greatestIncAmt[1] = increase
            
            if(increase < greatestDecAmt[1]):
                greatestDecAmt[0] = row[0]
                greatestDecAmt[1] = increase

        lastvalue=row[1]
        totalchange = (int(lastvalue) - int(firstvalue))
        avgchange = round(totalchange/(totalmonths-1),2)

output=(
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {totalmonths}\n"
    f"Total Change:${total}\n"
    f"Average Change: ${avgchange}\n"
    f"Greatest Increase in Profits:{greatestIncAmt[0]}(${greatestIncAmt[1]})\n"
    f"Greatest Decrease in Profits:{greatestDecAmt[0]}(${greatestDecAmt[1]})\n")

print(output)

with open(pybank_analysis, "w") as txt_file:
    txt_file.write(output)