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
candidate_name_and_percent_dic = {}
combined_values = defaultdict(list)
winner_name = []
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
        
#make a new dictionary that is a copy of the names and votes
candidate_name_and_percent_dic = dict(candidate_name_and_votes_dic)

#modify new dictionaries vote total into percentage
for key in candidate_name_and_percent_dic: 
    candidate_name_and_percent_dic[key] = f"{round(((candidate_name_and_percent_dic[key] / (total_votes))*100),2)} %" 

#combine both dictionaries
for i in (candidate_name_and_percent_dic, candidate_name_and_votes_dic):
    for key, value in i.items():
        combined_values[key].append(value)


#Winner of popular vote
winner_name = max(candidate_name_and_votes_dic.items(), key = operator.itemgetter(1))[0]


#Outputs to be printed in txt file in analysis folder
output1 = (
    f"Election Results\n"
    f"----------------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"----------------------------------\n")

output2 = ('\n'.join("{}: {}".format(key, value) for key, value in combined_values.items()))

output3 = (
    f"\n----------------------------------\n"    
    f"Winner: {winner_name} \n"
    f"----------------------------------\n")


#print all outputs in txt file im analysis folder      
with open("analysis/output.txt", "w") as txt_file:
    txt_file.write(output1)
    txt_file.write(output2)
    txt_file.write(output3)
