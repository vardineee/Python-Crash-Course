def describe_city(city,country = "Iceland"):
    msg = f"{city.title()} is in {country.title()}"
    print(msg)

describe_city('Reykjavik ')
describe_city('santiago', 'chile')
describe_city(country = 'Chile', city='punta arenas')
    