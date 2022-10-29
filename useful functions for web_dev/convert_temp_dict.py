
german_cities_in_C = {'Hamburg': 15, 'Berlin': 17, 'Frankfurt': 19, 'München': 20, 'Rosenheim': 22}

# dict comprehension for converting celsius to fahrenheit
german_cities_in_F = {key: ((value*1.8)+32) for (key, value) in german_cities_in_C.items()}
print(german_cities_in_F)

# dict comprehension is also useful with a condition
# lets say, I only want to visit the warmest cities in germany:
cities_to_visit = {key: value for (key, value) in german_cities_in_C.items() if value >= 20}
print(cities_to_visit)
