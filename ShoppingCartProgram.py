
foods = []
prices = []
total = 0

while True:
    food = input("Enter a food you'd like to buy: (press q to quit) ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: "))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")

for food in foods:
    print(food)

for price in prices:
    total += price
    
print(f'Your total is: ${total}')