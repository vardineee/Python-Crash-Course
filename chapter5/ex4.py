age = int(input("Enter your age: "))
if age < 2:
    print("Person is a baby")
elif age < 4:
    print("The person is toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("You are teenager.")
elif age < 65:
    print("The person is adult.")
else:
    print("The person is elder.")
