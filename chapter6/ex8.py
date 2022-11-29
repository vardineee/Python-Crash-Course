pets = []
pet_0 ={
    'name': 'carcal',
    'owner': 'Nelly',
     'color': 'black',
    'age ': 2,
}
pets.append(pet_0)
pet_1 ={
    'name': 'cat',
    'owner': 'jone',
     'color': 'white',
    'age ': 1,
}
pets.append(pet_1)
for pet in pets:
    print(f"Here is what I know about {pet['owner'].title()}")
    for key, value in pet.items():
        print(f"\t - {key}: {value}")
    
