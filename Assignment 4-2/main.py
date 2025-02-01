name = input("Enter Employee's name: ")
numShifts = int(input("Enter Number of Shifts: "))
numTransactions = input("Enter Number of Transactions: "))
transactionValue = input("Enter Transaction dollar value: ")

productivityScore = transactionValue / numTransactions / numShifts

if productivityScore >= 200:

print("Employee Name: " + name)
print("Employee Bonus: $" + float(bonus))
