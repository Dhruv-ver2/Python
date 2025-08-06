bill=float(input("Enter the total bill amount: "))
people=int(input("Enter the number of people: "))

amount_per_person = bill / people
print(f"Each person should pay: ${amount_per_person:.2f}")