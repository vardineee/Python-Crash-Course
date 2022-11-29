rivers = {
    'nile': 'egypt',
    'Amazon': 'brazil',
    'Yangtze': 'chine',
}
for key, value in rivers.items():
    print(f"{key.title()} runs through {value.title()}\n")

for river in rivers.keys():
    print(f"{river.title()}")

print("\n")
for country in rivers.values():
    print(f"{country.title()}")
    