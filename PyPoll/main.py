import os
import csv

#specify path to csv file
poll_csv = os.path.join('Resources', 'election_data.csv')

count = []
candidates_unique = []#
candidate_vote_count = {}

with open(poll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)  

    for row in csvreader:
        count.append(row[0])
        candidates_name = (row[2])

        #if the candidate's name is found in the candidate_vote_count dictionary
        if candidates_name in candidate_vote_count:
            #then add 1 to the candidate's existing vote count
            candidate_vote_count[candidates_name] += 1
        
        #if the candidate's name isn't found in the candidate_vote_count dictionary
        else:
            #then add the candidates name into the dictionary with a starting vote count of 1
            candidate_vote_count[candidates_name] = 1

winner = max(candidate_vote_count, key=candidate_vote_count.get)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {len(count)}")
print("-------------------------")
for name in candidate_vote_count:
    percentage = float(f"{candidate_vote_count[name] / (len(count)) *100}")
    print(f"{name}: {percentage:.3f}% ({candidate_vote_count[name]})")
print("-------------------------")
print(winner)
print("-------------------------")


output_path = os.path.join("analysis", "main.txt")

with open (output_path, "w") as file:
    file.write("Election Results" + "\n")
    file.write("-------------------------"+ "\n")
    file.write(f"Total Votes: {len(count)} \n")
    file.write("-------------------------" + "\n")
    for name in candidate_vote_count:
        percentage = float(f"{candidate_vote_count[name] / (len(count)) *100}")
        file.write(f"{name}: {percentage:.3f}% ({candidate_vote_count[name]}) \n")
    file.write("-------------------------" + "\n")
    file.write(f"{winner} \n")
    file.write("-------------------------" + "\n")   

print ("Results have also been exported to main.txt")