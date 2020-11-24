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
months_sum = 0
greatest_inc = {"month": "", "value": 0}
greatest_dec = {"month": "", "value": 0}


with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        total_months = total_months + (row[0])
        months_sum += 1
        average_change = months_sum / total_months

        if greatest_inc["value"] > row[1]:
            greatest_inc["month"] = row[0]
            greatest_inc["value"] = row[1]
        if greatest_dec["value"] < row[1]:
            greatest_dec["month"] = row[0]
            greatest_dec["value"] = row[1]


output = (
    f"Total Months: {total_months}\n",
    f"Total: {months_sum}\n",
    f"Average Change: ${average_change}\n",
    f"Greatest Increase in Profits: {}\n",
    f"Greatest Decrease in Profits: {}\n"
)

with open("analysis/output.txt", "w") as txt_file:
    txt_file.write(output)