# Modules
import os
import csv

# def function(export_filename):
#     #code here
#     with open(f"analysis/{export_filename}.txt", "w") as txt_file:
#         txt_file.write(ouput)

#set path for the file
csvpath = os.path.join("resources", "budget_data.csv")
total = 0
months = 0
greatest_inc = {"month": "", "value": 0}
greatest_dec = {}


with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        total = total + row[2]
        months += 1
        if greatest_inc["value"] < row[2]:
            greatest_inc["month"] = row[0]
            greatest_inc["value"] = row[2]


output = (
    f"Total: {total}\n",
    f"  \n"
)

with open("analysis/output.txt", "w") as txt_file:
    txt_file.write(output)