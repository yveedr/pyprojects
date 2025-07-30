foods = []
prices = []
quantity = 0
total = 0

while True:
    food = input("Enter a food you'd like to buy: (press q to quit)")
    if food.lower() == "q":
        break
    else:
        quantity = int(input("Enter a quantity: "))
        price = float(input(f"enter the price of {food}: "))
        foods.append(food)
        prices.append(price * quantity)

print("-----YOUR CART-----")
    
for food in foods:
    print(food, end=" ")
print()

for price in prices:
    total += price

print(f"your total is: ${total}")
