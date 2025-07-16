
weight = float(input("Enter your weight: "))
unit = input("Convert to kilograms or pounds?: (K or L)")

if unit == "K" or unit== "k":
  weight = weight * 2.205
  print(f"your weight is : {round(weight, 2)} kg.")
 
elif unit == "L" or unit == "l":
  weight = weight / 2.205
  print(f"your weight is: {round(weight,2)} lbs.")
  
else:
  print(f"{unit} is not correct. Try again.")
