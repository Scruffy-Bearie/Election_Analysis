#Add the dependencies
import csv
import os

#Assign a variable for the file to load and the path
results_load = os.path.join("election_results.csv")

#Create a filename variable to a direct or indirect path to the file
election_save = os.path.join("election_results.txt")

#1 Initialise a total vote counter
total_votes = 0

#Create List for Candidate Names
candidate_options = []
county_options = []

#Create a dictionary to hold candidate votes
candidate_votes = {}
county_votes = {}

#Winning candidate and winning count tracker
winning_canidate = ""
winning_count = 0
winning_percentage = 0

winning_county = ""
winning_county_count = 0


#Open the election results and read the file
with open(results_load) as election_data:

    #To do: Reand Data and Perform analysis
    

    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Read and Print the header row
    headers = next(file_reader)
   

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

        county_name = row[1]
        if county_name not in county_options:
            county_options.append(county_name)

            county_votes[county_name] = 0

        county_votes[county_name] = county_votes[county_name] + 1

    # Save the results to our text file.
with open(election_save, "w") as txt_file:

    #Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"   
        f"-------------------------\n")
    print(election_results, end="")
   
        # Save the final vote count to the text file.
    txt_file.write(election_results)

    ccvotes = "\nCounty Votes:\n"
    print(ccvotes)
    txt_file.write(ccvotes)

#Determine the percentage for each county
    for county_name in county_votes:
        cvotes = county_votes[county_name]
        cvote_percentage = (float(cvotes/total_votes))*100
        county_results = (
            f"{county_name}: {cvote_percentage:.1f}% ({cvotes:,})")
    
        print(county_results)
        txt_file.write(county_results)

        if (cvotes > winning_county_count):
            winning_county_count = cvotes
        
            winning_county = county_name

     #Print election summary
    winning_county_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")       

    print(winning_county_summary)
    txt_file.write(winning_county_summary)

#Determine the percentage for each candidate by looping through candidate_votes library
#iterate through the candidate list
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = (float(votes/total_votes))*100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    #Print vote percentage
        
        print(candidate_results)
        txt_file.write(candidate_results)
    
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
    txt_file.write(winning_candidate_summary)



