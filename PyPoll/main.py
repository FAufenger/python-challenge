# Modules
import os
import csv


#set path for the file
csvpath = os.path.join("resources", "pypoll_election_data.csv")
total_votes = 0
candidate_names = []
percent_votes = 0
candidate_votes = {}
winner = str() #or ""


with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:

        #Total number of votes cast
        total_votes += 1

        #List of all unique canadites and total votes for each candidate
        if row[2] not in candidate_names:
            candidate_names.append(row[2])
            candidate_votes[row[2]] = 1 
            
        else:
            candidate_votes[row[2]] += 1

        #Percentage of votes each candidate received
        percent_votes = (candidate_votes / total_votes)

        #Winner of popular vote
        winner = #candidate votes > other candidates then
 

output = (
    f"Election Results\n",
    f"----------------------------------\n",
    f"Total Votes: {total_votes}\n",
    f"----------------------------------\n",
    f"{#candidate_names}: {percent_votes} ({candidate_votes})\n",
    f"----------------------------------\n",
    f"winner: {winner}\n",
    f"----------------------------------\n"
)

with open("analysis/output.txt", "w") as txt_file:
    txt_file.write(output)