prompt = "\nPlease enter your age"
prompt += "\nIf you wnat to exit enter 'quit'. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
         print("  Your ticket is $15.")