responses = {}
name = input("\nWhat is your name? ")
response = input("\nPlease enter your favorite place to visit.")
continue_prompt = input("Would you like to continue polling? Yes/No ")
while True:
     responses[name] = response
     repeat = (continue_prompt)
     if repeat != 'Yes':
       break
   
print("---Here is the poll results!---\n")
for name, place in responses.items():
    print(f"{name.title()} liks to visit {place.title()}")