# Import Module for OS reading CSV files
import os
import csv
#intialize list variables and counter variables
votes_cast=[]
canidate_list=[]
list_of_cand=[]
can_count=[]
Per_list=[]
results_list=[]
i=0
j=0
k=0


#Set file path
csvpath = os.path.join('..','Resources','election_data.csv')

#Reading using CSV module
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # for loop to look through each row of data and create list of all votes cast
    for row in csvreader:
        canidate_list.append(row[2])
    #Determine number of votes cast
    num_votes_cast=int(len(canidate_list))
    #Create a set of all canidates recieving votes
    unique_canidates=set(canidate_list)
    #Create a list of all Canidates recieving votes
    list_of_cand=list(unique_canidates)
    #for loop to create a list of number of votes indexed to list_of_cand
    for each_can in list_of_cand:
        Can_One=canidate_list.count(list_of_cand[i])
        can_count.append(Can_One)
        i+=1
    #for loop to create a list of percentage of votes indexed to list_of_cand
    for each_can in can_count:
        Percent_calc=can_count[j]/num_votes_cast*100
        Per_list.append(Percent_calc)
        j+=1
    #Determine index of highest vote getter
    most_votes= max(can_count)
    highest_vote_index=can_count.index(most_votes)
    #format Percent list to three decimal places
    round_percents = [round(num, 3) for num in Per_list]
    # create a list of canidate, percentage of votes, and number of votes
    for canidates in unique_canidates:
        results_list.append(f'{list_of_cand[k]}:{round_percents[k]}%  {can_count[k]}')
        k+=1
    #format list of voting results
    formatted_results='\n'.join(results_list)
    winner=f'Winner: {list_of_cand[highest_vote_index]}' 
    #create variables to format all ouput
    intro="Election Results"
    lnbreak="---------------------"
    state_total=f'Total Votes: {num_votes_cast}'
    
    
    
    

#create list to order elements to display overall results
lines=[intro,lnbreak,state_total,lnbreak,formatted_results,lnbreak,winner]

#for loop to print each line of display data
for line in lines:
    print(line)
    
    
    
#writing file to txt file
# Specify the file to write to
output_path = os.path.join("analysis", "analysis_output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:
   for line in lines:
    txtfile.write(line)
    txtfile.write('\n')
    
