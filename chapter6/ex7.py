user_1 = {
    'first_name': 'Nala',
    'last_name': 'smith',
    'age': 19,
    'city': 'Lion',
}

user_2 ={
    'first_name': 'Joe',
    'last_name': 'doE',
    'age': 56,
    'city': 'Moscow',
}
people = []
people.append(user_1)
people.append(user_2)
# print(people)

for user in people:
    name = f"{user['first_name']} {user['last_name']}"
    age = user['age']
    city = user['city']
    print(f"{name}, of {city}, is {age} years old")

