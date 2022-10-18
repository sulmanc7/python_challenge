# Import Module for OS reading CSV files
import os
import csv
#Intialize Variables
months =[]
value =[]
old_value=0
sum_difference =0
total=0
highest_change=0
lowest_change=0

#Set file path
csvpath = os.path.join('..','Resources','budget_data.csv')


#Reading using CSV module
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

   
   # for loop to look through each row of data
    for row in csvreader:
       #create lists for month column and value column 
       months.append(row[0])
       value.append(row[1])
       #Acquire current row value for value column
       new_value=int(row[1])
       #calculate change between current value and previous value
       difference= new_value-old_value
       #running total of change value
       sum_difference += difference
       #set old value equal to new value for next loop
       old_value = new_value 
       #running total of value
       total+=(int(row[1]))
      # if statement to check for greatest postive change and update tracking value
       if difference> highest_change:
            highest_change_month = (row[0])
            highest_change=difference
      # if statement to check for greatest negative change and update tracking value
       if difference< lowest_change:
            lowest_change_month = (row[0])
            lowest_change=difference
    
    #create int values for number on months and number of months less one for display and calculation of average change
    num_months=int(len(months))
    num_months_lessone=int(len(months))-1
    
    #calculation of average difference and formatting
    sum_difference =sum_difference-int(value[0])
    avg_dif=sum_difference/(num_months_lessone)
    round_avg_dif=round(avg_dif,2)
    
    #creating variables for display of data
    total_months=f'Total Number of Months:{num_months}'
    intro="Financial Analysis"
    state_high=f'Greatest increase in profits: {highest_change_month} ${highest_change}'
    state_low=f'Greatest decrease in profits: {lowest_change_month} ${lowest_change}'
  
    state_total=f'Total:${total}'
    state_avgdif= f'Average Change:${round_avg_dif}'

    
   
    
   
   #creating list of all display data
lines =[intro,total_months,state_total,state_avgdif,state_high,state_low]
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
