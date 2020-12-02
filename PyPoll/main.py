# Modules
import os
import csv
import operator
from collections import defaultdict

#set path for the file
csvpath = os.path.join("resources", "pypoll_election_data.csv")
total_votes = 0
candidate_names = []
percent_votes = 0
candidate_name_and_votes_dic = {}
candidate_name_votes_percent_dic = {}
candidate1 = []
candidate2 = []
candidate3 = []
candidate4 = []
winner = str() #or ""
winner_name = []
cancan_dic = {}
combined_values = defaultdict(list)

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


#for key in candidate_name_and_votes_dic.values():

#   if key in candidate_name_and_votes_dic
#        candidate_name_and_votes_dic.append()

#candidate_name_votes_percent_dic = candidate_name_and_votes_dic.update((x, y / (total_votes)*100)) for x, y in candidate_name_and_votes_dic.items())


#Percentage of votes each candidate received
percent_vote1 = f"{round(((candidate_name_and_votes_dic[candidate_names[0]]) / (total_votes)*100),2)} %" 
percent_vote2 = f"{round(((candidate_name_and_votes_dic[candidate_names[1]]) / (total_votes)*100),2)} %"
percent_vote3 = f"{round(((candidate_name_and_votes_dic[candidate_names[2]]) / (total_votes)*100),2)} %"
percent_vote4 = f"{round(((candidate_name_and_votes_dic[candidate_names[3]]) / (total_votes)*100),2)} %"


#Append current dictionary to have a list for values (name, percent and total votes)
candidate1 = candidate_names[0], percent_vote1, f"({candidate_name_and_votes_dic[candidate_names[0]]})"
candidate2 = candidate_names[1], percent_vote2, f"({candidate_name_and_votes_dic[candidate_names[1]]})"
candidate3 = candidate_names[2], percent_vote3, f"({candidate_name_and_votes_dic[candidate_names[2]]})"
candidate4 = candidate_names[3], percent_vote4, f"({candidate_name_and_votes_dic[candidate_names[3]]})"

#candidate_name_votes_percent_dic = candidate1, candidate2, candidate3, candidate4   
#print(candidate_name_votes_percent_dic)

#Winner of popular vote
winner_name = max(candidate_name_and_votes_dic.items(), key = operator.itemgetter(1))[0]


output = (
    f"Election Results\n"
    f"----------------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"----------------------------------\n"
    f"{candidate1}\n"
    f"{candidate2}\n"
    f"{candidate3}\n"
    f"{candidate4}\n"
    f"----------------------------------\n"    
    f"Winner: {winner_name} \n"
    f"----------------------------------"
)

cancan_dic = dict(candidate_name_and_votes_dic)

for key in cancan_dic: 
    cancan_dic[key] = f"{round(((cancan_dic[key] / (total_votes))*100),2)} %" 


for i in (cancan_dic, candidate_name_and_votes_dic):
    for key, value in i.items():
        combined_values[key].append(value)

print(combined_values)
#print(combined_values)
#print(candidate_name_and_votes_dic)
#for i in candidate_name_votes_percent_dic.keys():
#    print('{} : {}\n'.format(i,candidate_name_votes_percent_dic.get(i)))

#print('\n'.join("{}: {}".format(k, v) for k, v in candidate_name_votes_percent_dic.items()))

with open("analysis/output.txt", "w") as txt_file:
    txt_file.write(output)

    #for candidate in candidate_votes
