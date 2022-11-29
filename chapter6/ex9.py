favorite_places = {
    'lia': ['Italy', 'Czech'],
    'teri': ['Russia', 'Cyprus','Latvia',],
    'nala': ['France', 'UK']
}

for person, country in favorite_places.items():
    print(f"Here are the favorite place of {person.title()}")
    for place in country:
        print(f" \t- {place}")
    
