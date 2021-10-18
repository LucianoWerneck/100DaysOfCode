#Program for Calculating BMI
print("Calculating your BMI.")
height = float(input("Enter your height in m:\n "))
weight = float(input("Enter your weight in kg:\n "))
bmi = round(weight / height ** 2)
print(f"Your BMI is {bmi}")
if bmi < 18.5:
  print("You are underweight.")
elif bmi < 25:
  print("You have a normal weight.")
elif  bmi < 30:
  print("You are slightly overweight.")
elif bmi < 35:
  print("You are obese.")
else:
  print("You are clinically obese.")