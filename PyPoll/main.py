# Modules
import os
import csv
import operator


#set path for the file
csvpath = os.path.join("resources", "pypoll_election_data.csv")
total_votes = 0
candidate_names = []
candidate_name_and_votes_dic = {}
summary_candidates = ""
winner_name = []


with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for candidate_data in csvreader:

        #Total number of votes cast
        #Adds total of all rows (less the header due to above code)
        total_votes += 1

        #List of all unique canadites 
        #start dictionary(set values to zero)
        if candidate_data[2] not in candidate_names:
            candidate_names.append(candidate_data[2])
            candidate_name_and_votes_dic[candidate_data[2]] = 0

        #Add total of votes to dictionary keys (unique candidate names)
        candidate_name_and_votes_dic[candidate_data[2]] += 1
        
#combine all variables from dictionary and add in percent value
# into string to present in output
for key, value in candidate_name_and_votes_dic.items():
    summary_candidates += f"{key}: {round(((value/total_votes) *100),2)}% ({value})\n"


#Winner of popular vote
winner_name = max(candidate_name_and_votes_dic.items(), key = operator.itemgetter(1))[0]


#Outputs to be printed in txt file in analysis folder
output = (
    f"Election Results\n"
    f"----------------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"----------------------------------\n"
    f"{summary_candidates}"
    f"----------------------------------\n"    
    f"Winner: {winner_name} \n"
    f"----------------------------------")

#print results to terminal
print(output)

#print all outputs in txt file im analysis folder      
with open("analysis/output.txt", "w") as txt_file:
    txt_file.write(output)

