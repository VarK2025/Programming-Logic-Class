name = input("Enter Employee's name: ")
numShifts = int(input("Enter Number of Shifts: "))
numTransactions = input("Enter Number of Transactions: ")
transactionValue = input("Enter Transaction dollar value: ")

productivityScore = transactionValue / numTransactions / numShifts
bonus = 0.0

if productivityScore >= 200:
  bonus = 200.00
elif productivityScore >= 70:
  bonus = 100.0
elif productivityScore >= 31:
  bonus = 75.0
else:
  bonus = 50.0

print("Employee Name: " + name)
print("Employee Bonus: $" + float(bonus))
