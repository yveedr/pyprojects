unit = input("Celsius or Fehrenheit (C/F)? ")
temp = float(input("Enter a temperature: "))

if unit == "C" or unit == "c":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"your temperature is: {temp}°c")

elif unit == "F" or unit == "f":
    temp = round((temp -32) * 5 / 9, 1)
    print(f"your temperature is: {temp}°f")

else:
    print(f"{unit} is not valid. Try again.")