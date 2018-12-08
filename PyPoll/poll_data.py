# Importing os and csv module
import os
import csv
import operator

# Initializing local variables

row_count = 0
winner    = "x-y-z"
winner_set = "N"
candidate = {'x-y-z':-10}

# csv file path
csvpath = os.path.join("..", "python_data", "election_data.csv")

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

        if row[2] in candidate.keys():
           candidate[row[2]] = candidate[row[2]] + 1
        else:
           candidate.update({row[2]:1})

        #if candidate.has_key(row[2]):
           #candidate[row[2]] = candidate[row[2]] + 1
        #else:
           #candidate.update({row[2]:1})
            
csvfile.close()

sorted_candidate = sorted(candidate.items(), key=operator.itemgetter(1))

sorted_candidate.reverse()

#Open the txt file
write_file = open("poll_out.txt", "w+")

#writing on screen
print("Election Results")
print("--------------------------")           
print("Total Votes: " + str(row_count))
print("--------------------------")           

#writing on file
write_file.write("Election Results")
write_file.write("\n--------------------------")           
write_file.write("\nTotal Votes: " + str(row_count))
write_file.write("\n--------------------------")           

for key, value in sorted_candidate:
    if key != 'x-y-z':
        #writing on screen
        print(key +": " + "{:.3f}".format(100*float(value)/float(row_count)) + "% (" + str(value) + ")")
        #writing on file
        write_file.write("\n" + key +": " + "{:.3f}".format(100*float(value)/float(row_count)) + "% (" + str(value) + ")")
        
        if winner_set == "N":
           winner = key
           winner_set = "Y"

#printing on screen
print("--------------------------")           
print("Winner: " + winner)
print("--------------------------")           
            
#writing on file
write_file.write("\n--------------------------")           
write_file.write("\nWinner: " + winner)
write_file.write("\n--------------------------") 

#Close the file
csvfile.close()
write_file.close()