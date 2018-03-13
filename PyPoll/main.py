# -*- coding: UTF-8 -*-
import csv

datafile = "raw_data/election_data_2.csv"
analysisfile = "analysis/election_analysis_2.txt"

votetotal = 0

candilist = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0

with open(datafile) as election_data:
    reader = csv.DictReader(election_data)

    for row in reader:

        print(". ", end=""),

        votetotal = votetotal + 1

        candidate_name = row["Candidate"]

        if candidate_name not in candilist:

            candilist.append(candidate_name)

            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

with open(analysisfile, "w") as txt_file:

    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {votetotal}\n"
        f"-------------------------\n")
    print(election_results, end="")

    txt_file.write(election_results)

    for candidate in candidate_votes:

        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(votetotal) * 100

        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        txt_file.write(voter_output)

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)
