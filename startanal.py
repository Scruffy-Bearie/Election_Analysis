#Add the dependencies
import csv
import os

#Assign a variable for the file to load and the path
results_load = os.path.join("Election_Analysis","election_results.csv")

#Create a filename variable to a direct or indirect path to the file
election_save = os.path.join("Election_Analysis\Analysis","election_analysis.txt")

#1 Initialise a total vote counter
total_votes = 0

#Create List for Candidate Names
candidate_options = []

#Create a dictionary to hold candidate votes
candidate_votes = {}

#Winning candidate and winning count tracker
winning_canidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(results_load) as election_data:

    #To do: Reand Data and Perform analysis
    print(election_data)

    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Read and Print the header row
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        #2 add to the total vote count
        total_votes = total_votes + 1
    
        #Print candidate name from each row
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            #Add candidate name to candidate_options
            candidate_options.append(candidate_name)

            #Begin tracking candidates vote count
            candidate_votes[candidate_name] = 0

        #tally candidate votes
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

#Determine the percentage for each candidate by looping through candidate_votes library
#iterate through the candidate list
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = (float(votes/total_votes))*100

    #Print vote percentage
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name



    #Print election summary
winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
print(winning_candidate_summary)
    



#Print the candidate list
#print(candidate_options)

#Print tally of candidate votes
#print(candidate_votes)

#3 Print the total votes
#print(total_votes)


#Using the with statement open the file as a text file
with open(election_save, "w") as txt_file:

    #Write some text to the file
    txt_file.write("Arapahoe\nDenver\nJefferson")

