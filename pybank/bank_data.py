# Importing os and csv module
import os
import csv

# Initializing local variables

row_count        = 0
total_amt        = 0
total_change     = 0
amount           = 0
previous_amt     = 0
max_change       = 0
max_change_month = ""
min_change       = 0
min_change_month = ""


# csv file path
csvpath = os.path.join("..", "python_data", "budget_data.csv")

# Opening csv file

with open(csvpath) as csvfile:

    # Reading csv file
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first, which we will not use in the program
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        
        #Increasing row count
        row_count += 1
                
        #Reading amount for the month        
        amount = float(row[1])
        
        #Adding up to total
        total_amt += amount
        
        #Adding up to total change, activity from 2nd row onwards
        
        if row_count > 1:
           total_change += (amount - previous_amt)
           
        #Comparing Greatest Increase and Greatest Decrease         
        if (amount - previous_amt) > max_change:
           max_change = amount - previous_amt
           max_change_month = row[0] 
        elif (amount - previous_amt) < min_change:
           min_change = amount - previous_amt
           min_change_month = row[0]

        #Storing current amount as previous for processing
        previous_amt = amount

#Print on screen

print("Total Months: " + str(row_count))
print("Total: $" + "{:.0f}".format(total_amt))
print("Average Change: $" + "{:.2f}".format(total_change/(row_count - 1)))
print("Greatest Increase in Profits: " + max_change_month + " ($" + "{:.0f}".format(max_change) + ")")
print("Greatest Decrease in Profits: " + min_change_month + " ($" + "{:.0f}".format(min_change) + ")")

#Writing in textfile

#Open the txt file
write_file = open("bank_out.txt", "w+")

#Write into the file
write_file.write("Bank Data Analysis")
write_file.write("\n------------------\n")
write_file.write("\nTotal Months: " + str(row_count))
write_file.write("\nTotal: $" + "{:.0f}".format(total_amt))
write_file.write("\nAverage Change: $" + "{:.2f}".format(total_change/(row_count - 1)))
write_file.write("\nGreatest Increase in Profits: " + max_change_month + " ($" + "{:.0f}".format(max_change) + ")")
write_file.write("\nGreatest Decrease in Profits: " + min_change_month + " ($" + "{:.0f}".format(min_change) + ")")

#Close the files
csvfile.close()
write_file.close()