
principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle amount can't be less or equal to 0")
        
while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Rate  can't be less or equal to 0")
        
while time <= 0:
    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("Time can't be less or equal to 0")
        


total = principle * pow((1 + rate / 100), time)
print(f"Total balance in {time:.0f} years is ${total}")