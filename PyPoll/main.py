import csv
import os 


candidate_list =[]
candidict = {}


#adding the path of the budget_data
csvpath = os.path.join("election_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#read the header row first (to make sure I'm in)
    csv_header = next(csvreader)
    
    total_votes = 0
    for row in csvreader:
        #Count the number of Votes cast
        total_votes = total_votes + 1
        #Adding Candidates to a list
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            #Add candidate to dictionary
            candidict[row[2]] = 1
        else:
            #Adding votes to my dictionary depending on candidate name
            candidict[row[2]] += 1

winner = max(candidict, key=candidict.get)



print("Election Results:")
print("---------------------------")
print("Total Votes: " + str(total_votes))
print("---------------------------")
for key in candidict:
    print(key, ":", "{:.3f}".format((candidict[key]/total_votes)* 100),"%  (",candidict[key],")")
print("---------------------------")
#prints out the winner
print("Winner: " + str(winner))
print("---------------------------")



f= open("new.txt","w+")
f.write("Election Results: \n")
f.write("--------------------------- \n")
f.write("Total Votes:" + str(total_votes) + '\n')
f.write("--------------------------- \n")
for key in candidict:
    f.write(str(key) + ": " + str("{:.3f}".format((candidict[key]/total_votes)* 100)) + "% (" + str(candidict[key]) + ")" + '\n')
f.write("--------------------------- \n")
f.write("Winner: " + str(winner) + '\n')
f.write("--------------------------- \n")
