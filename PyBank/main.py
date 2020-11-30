# Modules
import os
import csv

# def function(export_filename):
#     #code here
#     with open(f"analysis/{export_filename}.txt", "w") as txt_file:
#         txt_file.write(ouput)

#set path for the file
csvpath = os.path.join("resources", "pybank_budget_data.csv")
total_months = 0
net_total = 0
greatest_inc = {"month": "", "value": 0}
greatest_dec = {"month": "", "value": 0}
monthly_change = []
previous_value = 0

with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        #profit_loss= int(row[1])

        #Total number of months
        total_months = total_months + 1

        #Net profits (Sum of all profits and loses)
        net_total = net_total + int(row[1])  
        
        #Changes in profit
        if greatest_inc["value"] < int(row[1]):
            greatest_inc["month"] = row[0]
            greatest_inc["value"] = int(row[1])
        if greatest_dec["value"] > int(row[1]):
            greatest_dec["month"] = row[0]
            greatest_dec["value"] = int(row[1])

         #average changes for entire period
        profit_change = int(row[1]) - previous_value
        monthly_change.append(profit_change)
        previous_value = int(row[1])
    average_change = sum(monthly_change) / total_months

output = (
    f"Financial Analysis\n"
    f"----------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: {net_total}\n"
    f"Average Change: ${round(average_change,2)}\n"
    f"Greatest Increase in Profits: {greatest_inc['month']}  (${greatest_inc['value']})\n"
    f"Greatest Decrease in Profits: {greatest_dec['month']}  (${greatest_dec['value']})\n"
)

with open("analysis/output.txt", "w") as txt_file:
    txt_file.write(output)