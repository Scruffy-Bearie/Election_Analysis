#Add the dependencies
import csv
import os

#Assign a variable for the file to load and the path
results_load = os.path.join("Election_Analysis","election_results.csv")

#Create a filename variable to a direct or indirect path to the file
election_save = os.path.join("Election_Analysis\Analysis","election_analysis.txt")

#Open the election results and read the file
with open(results_load) as election_data:

    #To do: Reand Data and Perform analysis
    print(election_data)

    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Read and Print the header row
    headers = next(file_reader)
    print(headers)



#Using the with statement open the file as a text file
with open(election_save, "w") as txt_file:

    #Write some text to the file
    txt_file.write("Arapahoe\nDenver\nJefferson")

