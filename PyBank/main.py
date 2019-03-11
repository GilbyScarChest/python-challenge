#Assignment 3
#PyBank

import pandas as pd

csv_path = ("../Resources/budget_data.csv")

PyBank_df = pd.read_csv(csv_path)


Total_Months = PyBank_df.Date.count()
Sum_Total = PyBank_df['Profit/Losses'].sum()
Greatest_Increase = PyBank_df['Profit/Losses'].max()
Greatest_Decrease = PyBank_df['Profit/Losses'].min()
Average_diff = Greatest_Increase - Greatest_Decrease / PyBank_df.Date.count()


print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {Total_Months}")
print(f"Total: {Sum_Total}")
print(f"Average Change: ${Average_diff}")
print(f"Greatest Increase In Profits: {Greatest_Increase}")
print(f"Greates Decrease In Profits: {Greatest_Decrease}")