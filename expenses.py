#expenses = [10.50, 8, 5, 15, 20, 5, 3]
total = 0
expenses = []
#sum = 0
for i in range(7):
    expenses.append(float(input("Enter an expense:")))
#for x in expenses:
#    sum = sum + x
total = sum(expenses)
print('You spent $', total, sep = '')

