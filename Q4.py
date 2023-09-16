city_names = ["New York", "Los Angeles", "Chicago", "Houston", "Miami"]

with open('cities.txt', 'w') as file:
    for city in city_names:
        file.write(city + '\n')
