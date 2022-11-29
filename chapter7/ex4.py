prompt = "\nPlease enter series of pizza topings. "
prompt += "\Please enter 'quit' to end the program. "

toppings = ""
while toppings != 'quit':
    toppings = input(prompt)
    if toppings == 'quit':
        break
    else:
        print(toppings)

