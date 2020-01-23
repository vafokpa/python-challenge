import csv
import os 

#Store a list of integers for profits and losses
profit_losses = []
#Store a list of months
month_list = []
#store a list of integers of the changes in profits on a month by month basis
change_list =[]
#adding the path of the budget_data
csvpath = os.path.join("budget_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#read the header row first (to make sure I'm in)
    #print(f"CSV Header: {csv_header}")
    csv_header = next(csvreader)
    months = 0
    total_profit = 0
    # Read each row of data after the header
    for row in csvreader:
        # Count to see the amount of months of data
        months = months + 1
        # add profit and losses to a list
        profit_losses.append(int(row[1]))
        # find the total amount made over the course of all the data
        total_profit = total_profit + int(row[1])
        #add months to the list of months
        month_list.append(row[0])
        
for i in range(0,len(profit_losses)):
    difference = 0
    if i == 0:
        change_list.append(0)
    else:
        difference = profit_losses[i] - profit_losses[i-1]
        change_list.append(difference)

#Creating a variable for the sum of all changes
sum_change = 0
for change in change_list:
    sum_change = sum_change + change


#Finding the greatest increase in profits
big_increase = 0
index_increase = 0
for change in range(0,len(change_list)):
    if change_list[change] > big_increase:
        big_increase = change_list[change]
        index_increase = change


#Finding the greatest loss
big_decrease = 0
index_decrease = 0
for change in range(0,len(change_list)):
    if change_list[change] < big_decrease:
        big_decrease = change_list[change]
        index_decrease= change



print("Financial Analysis")
print("_________________________")
print("                        ")
print("Total Months: " + str(months))
print("Total: $" + str(total_profit))
print("Average Change: $" + str("{:.2f}".format(sum_change/ (len(change_list) - 1))))
print("Greatest Increase in Profits: " + str(month_list[index_increase])+ " ($" + str(big_increase) + ")")
print("Greatest Decrease in Profits: " + str(month_list[index_decrease])+ " ($" + str(big_decrease) + ")")



f= open("new.txt","w+")
f.write("Financial Analysis \n")
f.write("_________________________ \n")
f.write("                         \n")
f.write("Total Months: " + str(months) + '\n')
f.write("Total: $" + str(total_profit) + '\n')
f.write("Average Change: $" + str("{:.3f}".format((sum_change/ (len(change_list) - 1)))) + '\n')
f.write("Greatest Increase in Profits: " + str(month_list[index_increase])+ " ($" + str(big_increase) + ")" + '\n')
f.write("Greatest Decrease in Profits: " + str(month_list[index_decrease])+ " ($" + str(big_decrease) + ")" + '\n')