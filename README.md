# Title
## Overview of Election Audit
Election of a public official generally involves the collection of large data sets that require accurate tabulation and analysis.  Although it is possible to perform tabulation and analysis of such data sets using spread sheets, the process can be time consuming and prone to error.  Through use of programming interfaces such as Visual Studio Code and programming languages such as Python it is possible to automate tabulation processes thus saving time and reducing or eliminating errors.  The client for this project, The Colorado Board of Elections, wished to investigate the use of Python to automate the vote counting process not only to audit the results of the recent Congressional election but also to investigate the use of similar automation in future elections.  The following results and analysis represent an attempt to address these interests and possibilities.

## Election Audit Results
The results of the election audit and the coding used to acquire those results are summarised below:
### •	Total Votes:
Using an operation to eliminate the header row in the original data set and a “for loop" to count through the remaining rows of data (see Figure 1: Coding to Determine Total Number of Votes), it was possible to determine the total number of votes cast in the election.

![](https://github.com/Scruffy-Bearie/Election_Analysis/blob/main/Figure1.png)

**Total Votes = 369,711**

### •	County Votes and Percentages:
Using a “conditional if” statement within the “for loop” described above, it was possible to create a list of county names and determine the number of votes cast in each county (see Figure 2: Coding to Determine Number of Votes in Each County).  Through comparison to the Total Votes determined above, it was then possible to determine the percentage of votes cast in each county.

![](https://github.com/Scruffy-Bearie/Election_Analysis/blob/main/Figure2.png)

**County Votes:** <br />
**Jefferson:** 38,855 votes cast; 10.5% of Total Votes <br />
**Denver:** 306,055 votes cast; 82.8% of Total Votes <br />
**Arapahoe:** 24,801 votes cast; 6.7% of Total Votes <br />

### •	Largest County Turnout: Denver

### •	Candidate Votes and Percentages:
Similar to the process used for counting the number of votes in each county, a “conditional if” statement was established within the “for loop” used to count the Total Votes and it was possible to create a list of candidate names and determine the number of votes cast for each candidate (see Figure 3: Coding to Determine Number of Votes for Each Candidate).  Through comparison to the Total Votes determined above, it was then possible to determine the percentage of votes cast for each candidate.

![](https://github.com/Scruffy-Bearie/Election_Analysis/blob/main/Figure3.png)

**Candidate Votes and Percentages:** <br /> 
**Charles Casper Stockham:** 85,213 votes; 23.0% of Total Votes <br />
**Diana DeGette:** 272,892 votes; 73.8% of Total Votes <br />
**Raymon Anthony Doane:** 11,606 votes; 3.1% of Total Votes <br />

### •	Winning Candidate
Through comparing the number of votes cast for each candidate and using an f-string print statement (see Figure 4: Coding to Determine and Display the Winning Candidate), it was possible to determine and display the overall winner of the Congressional Election.

Link to Figure4

**Winner:** Diana Degette <br />
**Winning Vote Count:** 272, 892 <br />
**Winning Percentage:** 73.8 % <br />

## Election Audit Summary
The results acquired during the audit of the congressional election data demonstrate that a programming language like Python can be used to produce an automated tabulation process that is both accurate and efficient.  Moreover, the program assembled for this audit was constructed in such a way that with only minor modifications it could be easily redeployed for tabulation of data resulting from future electoral processes for different positions.  If the data relating to candidates and counties/districts is presented in a different format, the program can be easily altered to look for/acquire the data from a different location.  Similarly, inclusion of an additional “conditional if” statement within the “for loop”, such as that displayed in Figures 3 and 4, would make it possible to account for or track the votes cast via different voting methods.  Given the success of this audit and the ease with which it’s products could be applied to adapted, it is hoped that the Colorado Board of Elections will see fit to employ this automated data tabulation process for future projects.
