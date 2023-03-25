import pandas as pd
import os
import csv

 
election = pd.read_csv(r"C:\Users\therb\OneDrive\Documents\School\Python Challenge\Instructions\PyPoll\Resources\election_data.csv")

 
totalvotes = len(election)

 
candidatecount = election["Candidate"].value_counts()

 
percentvotes = (candidatecount/totalvotes)*100

 
winner = candidatecount.idxmax()

 
print("Election results")

 
print("Total votes: " + str(totalvotes))

print("Diana DeGette:" + " " + str(round(percentvotes[0],3)) + "%" + "("+str(candidatecount[0])+")")

print("Charles Casper Stockham:" + " " + str(round(percentvotes[1],3)) + "%" + "("+str(candidatecount[1])+")")

print("Raymon Anthony Doane:" + " " + str(round(percentvotes[2],3)) + "%" + "("+str(candidatecount[2])+")")

 
print("Winner: " + winner)

 
file = open('pypoll.txt','w')

file.write("Election results")

 
file.write("\nTotal votes: " + str(totalvotes))

file.write("\nCharles Casper Stockham:" + " " + str(round(percentvotes[0],3)) + "%" + "("+str(candidatecount[0])+")")

file.write("\nDiana DeGette:" + " " + str(round(percentvotes[1],3)) + "%" + "("+str(candidatecount[1])+")")

file.write("\nRaymon Anthony Doane:" + " " + str(round(percentvotes[2],3)) + "%" + "("+str(candidatecount[2])+")")

 
file.write("\nWinner: " + winner)

file.close()
