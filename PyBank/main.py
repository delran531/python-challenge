# In this challenge, you are tasked with creating a Python script for 
# analyzing the financial records of your company. You will give a set 
# of financial data called budget_data.csv. The dataset is composed 
# of two columns: Date and Profit/Losses. 
# (Thankfully, your company has rather lax standards for accounting 
# so the records are simple.)

# Your task is to create a Python script that analyzes the records to 
# calculate each of the following:


# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire 
# period
# The greatest decrease in losses (date and amount) over the entire 
# period


# As an example, your analysis should look similar to the one below:


#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)

# In addition, your final script should both print the analysis to the 
# terminal and export a text file with the results.

# Dependencies
import os
import csv

# path = 'C:\\Users\\delan\\OneDrive\\Documents\\GitHub\\python-challenge\\PyBank\\Resources'
datapath = os.path.join("Resources",'budget_data.csv')

# Initialize variables
ttl_mnths = 0
ttl_profits = 0
cur_pl = 0
cur_chng = 0
rng_chng = 0
gr_inc = 0
gr_dec = 0
gi_mnth = ''
gd_mnth = ''
cur_mnth = ''

# Loop thru file
with open(datapath, 'r',newline='') as datafile:
    readfile = csv.reader(datafile, delimiter=',')
    # skip header
    next(readfile)
    for row in readfile:
        # Start at 2nd data row
        if ttl_mnths >= 1:
            # Find current change and check against extremes
            cur_chng = int(row[1]) - int(cur_pl)
            rng_chng = cur_chng + rng_chng
            if cur_chng < gr_dec:
                gr_dec = cur_chng
                gd_mnth = row[0]
            elif cur_chng > gr_inc:
                gr_inc = cur_chng
                gi_mnth = row[0]
        if row[0] != "Date":
            cur_mnth = row[0]
            ttl_mnths = ttl_mnths + 1
            ttl_profits = ttl_profits + int(row[1])
            cur_pl = int(row[1])
        #print(row[0] + ' ' + row[1] + ' ' + str(cur_chng)

# Print Report
print ('Financial Analysis')
print ('----------------------------')
print ('Total Months: ' + str(ttl_mnths))
print ('Total: $' + str(ttl_profits))
print ('Average Change: $' + str(rng_chng / (ttl_mnths - 1)))
print ('Greatest Increase in Profits: ' + gi_mnth + " ($" + str(gr_inc) + ")")
print ('Greatest Decrease in Profits: ' + gd_mnth + " ($" + str(gr_dec) + ")")

# Open Report file
outfile = open("Resources\\budget_data_report.txt","a")

# Write the rows
outfile.write('Financial Analysis\n')
outfile.write('----------------------------\n')
outfile.write ('Total Months: ' + str(ttl_mnths) + '\n')
outfile.write ('Total: $' + str(ttl_profits) + '\n')
outfile.write ('Average Change: $' + str(rng_chng / (ttl_mnths - 1)) + '\n')
outfile.write ('Greatest Increase in Profits: ' + gi_mnth + " ($" + str(gr_inc) + ")\n")
outfile.write ('Greatest Decrease in Profits: ' + gd_mnth + " ($" + str(gr_dec) + ")\n")
outfile.close()