#Understanding Data Types and How to Manipulate Stringsr
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill?\n$"))
tip = int(input("What percentage tip would you like to give(10, 12 or 15)?\n"))
people = int(input("How many people to split the bill?\n"))
total_amount_division = ((bill * tip/ 100) + bill) / people
print(f"Each person should pay:\n${total_amount_division:.2f}ea")
