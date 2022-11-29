user ={
    'nala': [8, 96],
    'teri': [89, 78, 99],
    'leo': [19, 66],
    'edward': [333, 323]
}
for person, numbers in user.items():
    print(f"{person.title()} likes the following numbers:")
    for number in numbers:
        print(f"{number}")