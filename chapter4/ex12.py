pizzas = ['Pepperoni', 'Meat', 'Margherita' ]
friend_pizzas = pizzas
pizzas.append("Chicken")
print(f"My favorite pizzas are.")
friend_pizzas.append("Tomoato Pizza")
for pizza in pizzas:
    print(pizza)

print("\n")
for pizza in friend_pizzas:
    print(f"My friend’s favorite pizzas are: {friend_pizzas}")