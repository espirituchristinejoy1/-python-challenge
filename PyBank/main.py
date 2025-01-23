# -*- coding: UTF-8 -*-
"""PyBank Homework Solution."""
# Dependencies
import csv
import os
 
# Files to load and output (Using raw strings for Windows paths)
file_to_load = r"C:\\Users\\Christine Espiritu\\OneDrive\Documents\Boot Camp\\Homework\\03 - python-challenge\\PyBank\\Resources\budget_data.csv"
file_to_output = r"C:\\Users\\Christine Espiritu\\OneDrive\Documents\Boot Camp\\Homework\\03 - python-challenge\\PyBank\\analysis\budget_analysis.txt"
 

# Define variables to track the financial data
total_months = 0
total_net = 0
 
# Add more variables to track other necessary financial data
net_change_list = []
date_list = []
 
print("Starting financial analysis...")
 
try:
    # Open and read the csv
    with open(file_to_load) as financial_data:
        reader = csv.reader(financial_data)
 
        # Skip the header row
        header = next(reader)
 
        # Extract first row to avoid appending to net_change_list
        first_row = next(reader)
        total_months = 1
        total_net = int(first_row[1])
        previous_net = int(first_row[1])
 
        # Process each row of data
        for row in reader:
            # Track the total
            total_months += 1
            total_net += int(row[1])
            current_net = int(row[1])
            date_list.append(row[0])
 
            # Track the net change         
            net_change_value = current_net - previous_net
            net_change_list.append(net_change_value)    
            previous_net = current_net  # Use current_net instead of row[1]
 
        # Calculate the greatest increase in profits (month and amount)
        max_value = max(net_change_list)
        max_index = net_change_list.index(max_value)
 
        # Calculate the greatest decrease in losses (month and amount)
        min_value = min(net_change_list)
        min_index = net_change_list.index(min_value)
 
        # Calculate the average net change across the months
        average_value = sum(net_change_list) / len(net_change_list)
 
        # Generate and print the results
        financial_analysis = (
            "\nFinancial Analysis\n"
            "-------------------------\n"
            f"Total Months: {total_months}\n"
            f"Total: ${total_net:,}\n"
            f"Average Change: ${average_value:,.2f}\n"
            f"Greatest Increase in Profits: {date_list[max_index]} (${max_value:,})\n"
            f"Greatest Decrease in Profits: {date_list[min_index]} (${min_value:,})\n"
        )
 
        # Print to terminal
        print(financial_analysis)
 
        # Write to text file
        with open(file_to_output, "w") as txt_file:
            txt_file.write(financial_analysis)
 
        print(f"\nResults have been written to: {file_to_output}")
 
except FileNotFoundError:
    print(f"Error: Could not find the file at {file_to_load}")
    print("Please check if:")
    print("1. The path is correct")
    print("2. The Resources folder exists")
    print("3. The budget_data.csv file is in the Resources folder")
except Exception as e:
    print(f"An error occurred: {str(e)}")