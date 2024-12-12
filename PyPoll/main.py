# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates = []  # List of candidate names
candidate_votes = {"":0}  # Dictionary to track candidate votes, empty candidate with 0 votes to start

# Winning Candidate and Winning Count Tracker
winning_candidate = ""  # Name of the winning candidate

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row

        total_votes += 1 # Add 1 to the total vote count 

        # Get the candidate's name from the row
        candidate_name = row[2]
        

            # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidates:
            candidates.append(candidate_name)  # Add the candidate name to the candidate list
            candidate_votes[candidate_name] = 1 # Set the candidate's vote count to 1
            # Add a vote to the candidate's count
        else:
            candidate_votes[candidate_name] += 1 # Add a vote to the candidate's count 

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print(f"\nElection Results\n-------------------------\nTotal Votes: {total_votes}\n-------------------------") 

    # Write the total vote count to the text file
    txt_file.write(f"\nElection Results\n-------------------------\nTotal Votes: {total_votes}\n-------------------------")

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidates:
        # Get the vote count and calculate the percentage
        votes = candidate_votes[candidate]
        vote_percentage = (votes / total_votes) * 100

        # Update the winning candidate if this one has more votes
        if candidate_votes[candidate] > candidate_votes[winning_candidate]: #this works because I included the empty candidate with 0 votes
            winning_candidate = candidate

        # Print and save each candidate's vote count and percentage
        print(f"{candidate}: {vote_percentage:.3f}% ({votes})")
        txt_file.write(f"\n{candidate}: {vote_percentage:.3f}% ({votes})")

        # Generate and print the winning candidate summary
    print(f"-------------------------\nWinner: {winning_candidate}\n-------------------------")

        # Save the winning candidate summary to the text file
    txt_file.write(f"\n-------------------------\nWinner: {winning_candidate}\n-------------------------")