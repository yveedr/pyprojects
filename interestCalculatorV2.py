
principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle amount can't be less than 0")
    else: 
        break
        
while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Rate  can't be less than 0")
    else:
        break

        
while True:
    time = float(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be less than 0")
    else:
        break
        


total = principle * pow((1 + rate / 100), time)
print(f"Total balance in {time:.0f} years is ${total:.2f}")