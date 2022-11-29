favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

people = ['lana', 'nala', 'sarah']
for person in people:
    if person in favorite_languages.keys():
        print(f"{person.title()}, thanks for response.")
    else:
        print(f"{person.title()} please make the poll.")