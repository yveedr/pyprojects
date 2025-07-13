# python calculator program #

operator = input("Enter an operator(+, -, * or /):")
numb1 = float(input("enter a number:"))
numb2 = float(input("enter a number:"))

if operator == "+":
    print(f"the result is: {numb1 + numb2}")
elif operator == "-":
    print(f"the result is: {numb1 - numb2}")
elif operator == "*":
    print(f"the result is: {numb1 * numb2}")
elif operator == "/":
    print(f"the result is: {numb1 / numb2}")
else:
    print(f"{operator} is not correct. Please, try again")