# Election_Analysis- Audit of an Election utilizing Python Code

## Overview of the Election Audit

The purpose of the election audit was to analyze the results of this election and provide results to the election commission. Audit results  include both canddate and county results. Candidate results include the total votes in the election, each candidate's total votes and percentage of votes and the winner of the election that includes winning vote count and winning percentage of vote. County results that were generated include the voter turnout for each county, the percentage of votes from each county out of the total count and the county with the highest turnout.  In addition Python code was used to generate the results in both the terminal output and saved into a text file.

## Election Audit Results	

The Election results located in the resources folder (election_results.csv) along with python code utilizing for loops, conditional statements and logical operators were used to complete the audit as seen below (terminal output) in addition to the output text file which is located in the analysis folder (election_results.txt).

![Election_Results](https://github.com/y2k600f4/Election_Analysis/blob/main/analysis/election_analysis.png)

### Candidate Results

#### Total votes in the election

The total votes in the election are shown to be 369,711.

#### Each candidate's total votes and percentage of votes

The (3) candidate with the total votes and percentage of votes were found to be:

Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)


#### Winner of the election, winning vote count, winning percentage of votes

The winner of the election with winning vote count and winning percentage of votes was shown to be:

Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%

### County Results

#### Voter turnout for each county

From the above terminal output (and election_results.txt file output) the total votes for each of the (3) counties is shown. Jefferson county with 38855 votes, Denver County with 306055 votes and Arapahoe county with 24801 votes. The votes from all the counties add up to the total votes of 369,711.

#### Percentage of votes from each county out of the total county

From the above terminal output (and election_results.txt file output) the percentage of votes from each of the (3) counties calculated from the total votes in the election are shown to be Jefferson county with 10.5% of the votes, Denver county with 82.8% of the votes and Arapahoe county with 6.7% of the votes. The total percentage of votes form all (3) counties add up to 100% of the votes.

#### County with the highest turnout.

The county with the largest number of votes (306,055) is shown to be Denver.

## Election Audit Summary

This election script that was generated to generate election results from a file. The file contained multiple columns, with the columns of interest being "County" and "Candidate" in the case of this specific election a total of (3) counties and (3) candidates were contained in the election_results.csv file. By defining the candidate_options and county_options as lists and the candidate_votes and county_votes as dictionaries (as seen in the below code) this script can easily be utilized for both additional candidates and counties.

![code](https://github.com/y2k600f4/Election_Analysis/blob/main/analysis/code.png)

This script can easily be expanded to analyze addtitional election results by adding additional columns of data in the election_results.csv file such as additional locations such as town or city within the county or even higher levels such as state. The additional items would be extracted from each row (e.g. town, city, state) and adding additional if statements and for loops following the same structure in this exercise can be added for additional analysis as needed.








