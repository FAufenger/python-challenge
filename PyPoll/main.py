# Modules
import os
import csv


#set path for the file
csvpath = os.path.join("resources", "pypoll_election_data.csv")
total_votes = 0
candidate_names = []
percent_votes = 0
candidate_name_and_votes_dic = {}
winner = str() #or ""

with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for candidate_data in csvreader:

        #Total number of votes cast
        total_votes += 1

        #List of all unique canadites and start dictionary(set to zero)
        if candidate_data[2] not in candidate_names:
            candidate_names.append(candidate_data[2])
            candidate_name_and_votes_dic[candidate_data[2]] = 0

        #Add total of votes per candidate to dictionary keys
        candidate_name_and_votes_dic[candidate_data[2]] += 1

    #Percentage of votes each candidate received
    percent_vote1 = round((int(candidate_name_and_votes_dic['Khan']) / int(total_votes)*100),2)
    percent_vote2 = round((int(candidate_name_and_votes_dic['Correy']) / int(total_votes)*100),2)
    percent_vote3 = round((int(candidate_name_and_votes_dic['Li']) / int(total_votes)*100),2)
    percent_vote4 = round((int(candidate_name_and_votes_dic["O'Tooley"]) / int(total_votes)*100),2)


    #Winner of popular vote
    #winner = #candidate votes > other candidates then


output = (
    f"Election Results\n"
    f"----------------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"----------------------------------\n"
    f"{candidate_name_and_votes_dic}\n"
    f"----------------------------------\n"
    f"{percent_vote1}%\n"
    f"{percent_vote2}%\n"
    f"{percent_vote3}%\n"
    f"{percent_vote4}%\n"
    
 #    f"winner: {winner}\n"
    f"----------------------------------"
)


with open("analysis/output.txt", "w") as txt_file:
    txt_file.write(output)

    #for candidate in candidate_votes
