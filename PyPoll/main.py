# In this challenge, you are tasked with helping a small, rural town modernize its vote-counting 
# process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but 
# unfortunately, his concentration isn't what it used to be.)

# You will be give a set of poll data called election_data.csv. The dataset is composed of three 
# columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes 
# the votes and calculates each of the following:
#   * The total number of votes cast
#   * A complete list of candidates who received votes
#   * The percentage of votes each candidate won
#   * The total number of votes each candidate won
#   * The winner of the election based on popular vote.


# As an example, your analysis should look similar to the one below:


#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------

# In addition, your final script should both print the analysis to the terminal and export a 
# text file with the results.

# Dependencies
import os
import csv
from pathlib import Path

filepath = Path("Resources/election_data.csv")

# Get candidates
with open(filepath, 'r',newline='') as datafile:
    readfile = csv.reader(datafile, delimiter=',')
    candidates = set()
    # skip header
    next(readfile)
    for row in readfile:
        candidates.add(row[2])

# Initialize variables
total_votes = 0
can_votes = {}
votes = []
for can in candidates:
    #print(can)
    votes.append(0)
    can_votes[can] = 0

# Count votes
with open(filepath, 'r',newline='') as datafile:
    readfile = csv.reader(datafile, delimiter=',')
    # skip header
    next(readfile)
    for row in readfile:
        can_votes[row[2]] = can_votes[row[2]] + 1

# Do math for total votes
for can in candidates:
    total_votes = total_votes + can_votes[can]

# Print/Write Report
outfile = open("Resources\\election_data_report.txt","a")
print ('Election Results')
outfile.write ('Election Results\n')
print ('----------------------------')
outfile.write ('----------------------------\n')
print ('Total votes: ' + str(total_votes))
outfile.write ('Total votes: ' + str(total_votes) + '\n')
print ('----------------------------')
outfile.write ('----------------------------\n')
for can in candidates:
    print(can + ": " + str(round((can_votes[can]/total_votes)*100,0)) + "% (" + str(can_votes[can]) + ")")
    outfile.write (can + ": " + str(round((can_votes[can]/total_votes)*100,0)) + "% (" + str(can_votes[can]) + ")\n")
print ('----------------------------')
outfile.write ('----------------------------\n')
print ('Winner: ' + max(can_votes, key=can_votes.get))
outfile.write ('Winner: ' + max(can_votes, key=can_votes.get) + '\n')
print ('----------------------------')
outfile.write ('----------------------------\n')
