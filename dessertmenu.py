menu = {"cheesecake": 6.00,
        "brownie": 5.50,
        "tiramisu": 7.00,
        "pavlova": 6.50,
        "gelato": 4.00,
        "macaron": 2.50,
        "cupcake": 3.75,
        "mousse": 5.25,
        "pudding": 4.50}

cart = []
total = 0


print("------- DESSERT MENU -------")
for dessert, prices in menu.items():
    print(f"{dessert:16}: ${prices:.2f}")
print("----------------------------")

while True:
    food = input("Enter a item (press q to quit): ").lower()
    if food == "q" :
        break
    elif menu.get(food) is not None:
        cart.append(food)


print()
print("--------- YOUR CART ----------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Your total is: ${total:.2f}")
        
