new_city_names = ["San Francisco", "Boston", "Seattle"]

with open('cities.txt', 'a') as file:
    for city in new_city_names:
        file.write(city + '\n')
