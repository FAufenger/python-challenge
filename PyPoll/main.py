# Modules
import os
import csv
import operator
from collections import defaultdict

#set path for the file
csvpath = os.path.join("resources", "pypoll_election_data.csv")
total_votes = 0
candidate_names = []
candidate_name_and_votes_dic = {}
winner_name = []
candidate_name_and_percent_dic = {}
combined_values = defaultdict(list)
#candidate_name_votes_percent_dic = {}
#percent_votes = {}

with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for candidate_data in csvreader:

        #Total number of votes cast
        #Adds total of all rows (-header due to above code)
        total_votes += 1

        #List of all unique canadites 
        #start dictionary(set keys to zero)
        if candidate_data[2] not in candidate_names:
            candidate_names.append(candidate_data[2])
            candidate_name_and_votes_dic[candidate_data[2]] = 0

        #Add total of votes to dictionary keys (unique candidate names)
        candidate_name_and_votes_dic[candidate_data[2]] += 1
        

candidate_name_and_percent_dic = dict(candidate_name_and_votes_dic)

for key in candidate_name_and_percent_dic: 
    candidate_name_and_percent_dic[key] = f"{round(((candidate_name_and_percent_dic[key] / (total_votes))*100),2)} %" 

for i in (candidate_name_and_percent_dic, candidate_name_and_votes_dic):
    for key, value in i.items():
        combined_values[key].append(value)

#candidate_name_votes_percent_dic = candidate1, candidate2, candidate3, candidate4   
#print(candidate_name_votes_percent_dic)

#Winner of popular vote
winner_name = max(candidate_name_and_votes_dic.items(), key = operator.itemgetter(1))[0]



output = (
    f"Election Results\n"
    f"----------------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"----------------------------------\n")

output2 = ('\n'.join("{}: {}".format(k, v) for k, v in combined_values.items()))


output3 = (
    f"\n----------------------------------\n"    
    f"Winner: {winner_name} \n"
    f"----------------------------------\n"
)

#Optinal way to attempt to combine dictionaries
# for i in combined_values.keys():
#     output2 = ('{} : {}\n'.format(i,combined_values.get(i)))
# print(output2)



       
with open("analysis/output.txt", "w") as txt_file:
    txt_file.write(output)
    txt_file.write(output2)
    txt_file.write(output3)
