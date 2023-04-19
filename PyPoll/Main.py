import csv
import os
# #-------------------------------------------


# Set file paths for input file
file_path = "Resources/election_data.csv"


# Set file paths for output file
output_file_path = "Analysis/election_results.txt"


# Create empty list for candidate names and dictionary to store vote counts
candidates = []
vote_counts = {}


# Open input file and read data into a dictionary
with open(file_path) as file:
    reader = csv.DictReader(file)
    for row in reader:


        # Add candidate name to list if not already present
        if row["Candidate"] not in candidates:
            candidates.append(row["Candidate"])
            vote_counts[row["Candidate"]] = 0

        # Increment candidate's vote count
        vote_counts[row["Candidate"]] += 1


# #------------------------------------


# Calculate total number of votes cast
total_votes = sum(vote_counts.values())

# Determine the winner of the election based on popular vote
winner = max(vote_counts, key=vote_counts.get)



#----------------------------------------
# Print election results to console and output file
with open(output_file_path, "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")
    for candidate in candidates:
        vote_percentage = vote_counts[candidate] / total_votes * 100
        output_file.write(f"{candidate}: {vote_percentage:.3f}% ({vote_counts[candidate]})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")


    #--------------------------------------
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate in candidates:
        vote_percentage = vote_counts[candidate] / total_votes * 100
        print(f"{candidate}: {vote_percentage:.3f}% ({vote_counts[candidate]})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")