pizzas = ['Pepperoni', 'Meat', 'Margherita' ]
friend_pizzas = pizzas
pizzas.append("Chicken")
friend_pizzas.append("Tomoato Pizza")
for pizza in pizzas:
  print(f"My favorite pizzas are {pizza}")
print("\n")
for pizza in friend_pizzas:
 print(f"My friend’s favorite pizzas are: {pizza}")