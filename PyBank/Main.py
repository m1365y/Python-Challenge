import csv
import os
#-------------------------------------------



# Set path for file
# file='/PyBank/Resources/'
budget_csv = os.path.join( 'Resources/',"budget_data.csv")

# Create variables to store financial analysis data
total_months = 0
net_total = 0
changes = []
months = []


#------------------------------------
# Read CSV file and iterate over each row of data
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        # Calculate total number of months and net total amount of profit/losses
        total_months += 1
        net_total += int(row[1])

        # Calculate changes in profit/losses
        if total_months > 1:
            change = int(row[1]) - previous
            changes.append(change)
            months.append(row[0])

        previous = int(row[1])

#------------------------
# Calculate average change in profit/losses
avg_change = round(sum(changes) / len(changes), 2)

# Find greatest increase and decrease in profits
max_increase = max(changes)
max_decrease = min(changes)
max_increase_month = months[changes.index(max_increase)]
max_decrease_month = months[changes.index(max_decrease)]

# Print financial analysis results
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")

#----------
print(f"Total: ${net_total}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {max_increase_month} (${max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})")

# Export financial analysis results to a text file
output_file = os.path.join('analysis/',"financial_analysis.txt")

with open(output_file, "w") as file:
    file.write("Financial Analysis\n")
    file.write("-------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_total}\n")
    file.write(f"Average Change: ${avg_change}\n")
    file.write(f"Greatest Increase in Profits: {max_increase_month} (${max_increase})\n")
    file.write(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})\n")