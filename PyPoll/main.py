import csv
import os

votes = 0
winner_votes = 0
total_candidates = 0
greatest_votes = ["", 0]
candidate_options = []
candidates_vote_count = {}
candidates_vote_percentage = {}

csvpath = os.path.join('election_data.csv')

with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile)
        csv_header = next(csvfile)
        print(csv_header)

        for row in csvreader:
                #total votes
                votes = votes + 1

                #Candidates
                if row[2] not in candidate_options:
                        candidate_options.append(row[2])

                #Candidates vote count
                if row[2] not in candidates_vote_count:
                        candidates_vote_count[row[2]] = 1
                else:
                        candidates_vote_count[row[2]] += 1

                key = max(candidates_vote_count, key = lambda k:candidates_vote_count[k])


        for x in candidates_vote_count:
                candidates_vote_percentage[x] = (candidates_vote_count[x] / votes) * 100

        print(f'Total Votes = {votes}')
        print(f'Candidates = {candidate_options}')
        print(f'Vote Counts per Candidate = {candidates_vote_count}')
        print(f'Vote percentage = {candidates_vote_percentage} %')
        print(f'Winner is: {key}')