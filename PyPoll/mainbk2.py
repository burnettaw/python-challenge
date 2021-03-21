# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won


# The winner of the election based on popular vote.
import os
import csv

voter_id = []
county = []
candidate = []
unique_candidates = []
unique_candidates_total = []
total_votes_cast = 0
count_candidate = 0
output_analysis = ""

# read the file and calculate total
election_csv = os.path.join("Resources", "election_data.csv")

with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    #print header
    header = next(csv_reader)
    print(f"header: {header}")
   
    #line_num = 0
    index = 0
    for row in csv_reader:
                       
        voter_id.append(row[0])
        #county.append(row[1])
        candidate.append(row[2])  

        #Calculate the net total amount of votes
        total_votes_cast += 1


#Calculate unique list of candidates who recieved votes
#get unique candidate 
unique_candidates = list(set(candidate))


#count each unique candidate votes
#match_u2 = []
m2 = 0
for n in unique_candidates:
    unique_candidates_total.append(candidate.count(n)
    #match_u2.append(n)
    #m2 += 1

# sorts values before printing
#unique_candidates_total.sort(reverse = True)
# match the unique candidates with its totals for prining

#prints output to screen and file 
"""
output_analysis = (
    f"Election Results\n"
    f"----------------------------\n"
    f"Total Votes: {total_votes_cast}\n"
    f"----------------------------\n")  
   

oa = ""
i = 0 
for u in unique_candidates:
    oa += f"{u}: {unique_candidates_total[i]} \t {(unique_candidates_total[i]/total_votes_cast)}\n" 
    i+=1

print(output_analysis)  
print(oa)    
            
election_csv2 = os.path.join("Analysis", "election_data3.txt")
# Export the results to text file
with open(budget_csv2, "x") as txt_file:
    txt_file.write(output_analysis) """