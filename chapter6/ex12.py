cities = {
    'santiago': {
        'country': 'chile',
        'population': 6_310_000,
        'nearby mountains': 'andes',
        },
    'talkeetna': {
        'country': 'united states',
        'population': 876,
        'nearby mountains': 'alaska range',
        },
    'kathmandu': {
        'country': 'nepal',
        'population': 975_453,
        'nearby mountains': 'himilaya',
        }
    }
for city, info in cities.items():
        country = info['country']
        population =info['population']
        mountains = info ['nearby mountains']
    
        print(f"{city.title()} is in {country}")
        print(f"\tIt has popluation about {population}")
        print(f"\t{mountains} is nearby mountain.\n")