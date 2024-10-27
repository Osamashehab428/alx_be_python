monthlyincome = int(input("Enter your monthly income: "))
monthlyexpenses = int(input("Enter your monthly expenses: "))

monthlysavings = monthlyincome - monthlyexpenses

Projectedsavings = (monthlyexpenses  * 12 + (monthlysavings * 12 * 0.05))

print("Projected savings after one year, with interest, is: ", Projectedsavings)




