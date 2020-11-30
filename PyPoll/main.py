# Modules
import os
import csv


#set path for the file
csvpath = os.path.join("resources", "pypoll_election_data.csv")
total_votes = 0
candidate_names = str()
percent_votes = 0
candidate_votes = 0
winner = str()



with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:

        #Total number of votes cast
        total_votes = total_votes + row[0]

        #List of all canadites
        candidate_names = #unique values in first column .. maybe .. 
        #if (value <> vlaue then...cell value = cell value.. )

        #Total number of votes each candadate won
        candidate_votes = #if unique candidate then sum column 2

        #Percentage of votes each candidate received
        percent_votes = (candidate_votes / total_votes)"%"

        #Winner of popular vote
        winner = #candidate votes > other candidates then
 

output = (
    f"Election Results\n",
    f"----------------------------------\n",
    f"Total Votes: {total_votes}\n",
    f"----------------------------------\n",
    f"{candidate_names}: {percent_votes} ({candidate_votes})\n",
    f"----------------------------------\n",
    f"winner: {winner}\n",
    f"----------------------------------\n"
)

with open("analysis/output.txt", "w") as txt_file:
    txt_file.write(output)